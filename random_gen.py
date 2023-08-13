import time
import random
import numpy as np
import scipy.stats
import math
import datetime
import matplotlib.pyplot as plt

def poker_test(data):
    observed_frequencies = {
        'Five different digits': 0,
        'Pairs': 0,
        'Two pairs': 0,
        'Three of a kind': 0,
        'Full houses': 0,
        'Four of a kind': 0,
        'Five of a kind': 0
    }

    for number in data:
        digits = [int(digit) for digit in str(number)]
        digit_count = np.bincount(digits, minlength=10)
        unique_digits = np.count_nonzero(digit_count)

        if unique_digits == 5:
            observed_frequencies['Five different digits'] += 1
        elif unique_digits == 4:
            observed_frequencies['Pairs'] += 1
        elif unique_digits == 3 and np.max(digit_count) == 3:
            observed_frequencies['Three of a kind'] += 1
        elif unique_digits == 3:
            observed_frequencies['Two pairs'] += 1
        elif unique_digits == 2 and np.max(digit_count) == 4:
            observed_frequencies['Four of a kind'] += 1
        elif unique_digits == 2:
            observed_frequencies['Full houses'] += 1
        elif unique_digits == 1:
            observed_frequencies['Five of a kind'] += 1

    total_numbers = len(data)
    expected_frequencies = {
        'Five different digits': total_numbers * 0.3024,
        'Pairs': total_numbers * 0.5040,
        'Two pairs': total_numbers * 0.1080,
        'Three of a kind': total_numbers * 0.0720,
        'Full houses': total_numbers * 0.0090,
        'Four of a kind': total_numbers * 0.0045,
        'Five of a kind': total_numbers * 0.0001
    }

    observed_values = np.array(list(observed_frequencies.values()))
    expected_values = np.array(list(expected_frequencies.values()))

    chi_square_statistic, p_value = scipy.stats.chisquare(observed_values, expected_values)

    return p_value


def custom_random(seed=None):
    if seed:
        random.seed(seed)

    while True:
        system_time = math.modf(time.time())[0]
        cpu_cycles = int(time.process_time())
        country_time_offset = random.uniform(-12, 12)  # Different country time zones
        geometric_time_event = math.pow(0.5, random.randint(1, 10))
        noise = random.random()


        value = abs(system_time + cpu_cycles+ country_time_offset + geometric_time_event + noise) * 100000
        yield int(value) % 100000
        time.sleep(0.001)

def kolmogorov_smirnov_test(data):
    data1 = []
    for i in range(len(data)):
        data1.append(float(data[i]/100000))
    _, p_value = scipy.stats.kstest(data1, 'uniform')
    return p_value

def chi_squared_uniformity_test(data, num_bins=10):
    observed, _ = np.histogram(data, bins=num_bins, range=(10000, 100000))
    expected = len(data) / num_bins

    observed_total = np.sum(observed)
    expected_total = len(data)
    observed = observed * (expected_total / observed_total)

    chi_squared_statistic, p_value = scipy.stats.chisquare(observed, expected)
    return p_value


def autocorrelation_test(data, lag):
    autocorrelation_values = []
    for l in range(1, lag + 1):
        shifted_data = data[:-l]
        original_data = data[l:]
        corr_coefficient = np.corrcoef(shifted_data, original_data)[0, 1]
        autocorrelation_values.append(corr_coefficient)

    return autocorrelation_values
def autocorrelation_chi_square_test(autocorrelation_values):
    observed_frequencies = {
        'Negative Autocorrelation': sum(val < 0 for val in autocorrelation_values),
        'Positive Autocorrelation': sum(val > 0 for val in autocorrelation_values),
        'No Autocorrelation': sum(val == 0 for val in autocorrelation_values)
    }

    # Add a small constant to expected frequencies to avoid division by zero
    epsilon = 1e-9
    total_expected = len(autocorrelation_values) / 2
    expected_frequencies = {
        'Negative Autocorrelation': total_expected + epsilon,
        'Positive Autocorrelation': total_expected + epsilon,
        'No Autocorrelation': epsilon
    }

    observed_values = np.array(list(observed_frequencies.values()))
    expected_values = np.array(list(expected_frequencies.values()))

    chi_square_statistic, p_value = scipy.stats.chisquare(observed_values, expected_values)

    return p_value
def test_custom_random(num_samples=10000):
    generator = custom_random()
    data = [next(generator) for _ in range(num_samples)]

    kolmogorov_p_value = kolmogorov_smirnov_test(data)
    chi_squared_p_value = chi_squared_uniformity_test(data)
    autocorrelation_values = autocorrelation_test(data, 10)
    autocorrelation = autocorrelation_chi_square_test(autocorrelation_values)
    poker_test_result = poker_test(data)

    return data, kolmogorov_p_value, chi_squared_p_value, poker_test_result,autocorrelation

def test_builtin_random(num_samples=10000):
    data = [random.randint(0, 99999) for _ in range(num_samples)]

    kolmogorov_p_value = kolmogorov_smirnov_test(data)
    chi_squared_p_value = chi_squared_uniformity_test(data)
    poker_test_result = poker_test(data)
    autocorrelation_values = autocorrelation_test(data, 10)
    autocorrelation = autocorrelation_chi_square_test(autocorrelation_values)

    return data, kolmogorov_p_value, chi_squared_p_value, poker_test_result,autocorrelation

def visualize_distributions(data1, data2):
    plt.hist(data1, bins=50, alpha=0.5, label='Custom Random')
    plt.hist(data2, bins=50, alpha=0.5, label='Built-in Random')
    plt.legend(loc='upper right')
    plt.title('Distribution Comparison')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

def gap_test(data):
    n = len(data)
    gaps = [data[i] - data[i - 1] for i in range(1, n)]

    mean_gap = np.mean(gaps)
    gap_variance = np.var(gaps)
    gap_skewness = np.sum([(gap - mean_gap) ** 3 for gap in gaps]) / (n * gap_variance ** 1.5)

    chi_squared_statistic = (n / 2) * gap_skewness ** 2

    p_value = 1 - scipy.stats.chi2.cdf(chi_squared_statistic, df=1)

    return p_value

if __name__ == "__main__":
    custom_data, custom_kolmogorov, custom_chi_squared, custom_poker, custom_autocorrelation = test_custom_random()
    builtin_data, builtin_kolmogorov, builtin_chi_squared, builtin_poker,builtin_autocorrelation = test_builtin_random()
    gap_custom = gap_test(custom_data)
    gap_builtin = gap_test(builtin_data)
    print("Custom Random Generator:")
    print(f"Generated Data: {custom_data[:10]} ...")
    print(f"Kolmogorov-Smirnov p-value: {custom_kolmogorov}")
    print(f"Chi-Squared p-value: {custom_chi_squared}")
    print(f"Chi-Squared autocorrelation: {custom_autocorrelation}")
    print(f"Poker Test Result: {custom_poker}")


    print("\nBuilt-in Random Generator:")
    print(f"Generated Data: {builtin_data[:10]} ...")
    print(f"Kolmogorov-Smirnov p-value: {builtin_kolmogorov}")
    print(f"Chi-Squared p-value: {builtin_chi_squared}")
    print(f"Chi-Squared autocorrelation: {builtin_autocorrelation}")
    print(f"Poker Test Result: {builtin_poker}")

    if custom_chi_squared > 0.05 and gap_custom > 0.05 and custom_kolmogorov > 0.05:
        print("\nThe Custom Random Generator appears to perform comparably.")
    else:
        print("\nThe Custom Random Generator may exhibit differences.")

    if builtin_chi_squared > 0.05 and gap_builtin > 0.05 and builtin_kolmogorov > 0.05:
        print("The Built-in Random Generator appears to perform comparably.")
    else:
        print("The Built-in Random Generator may exhibit differences.")

    visualize_distributions(custom_data, builtin_data)
