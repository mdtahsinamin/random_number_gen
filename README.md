# Custom Random Number Generator

![Python Logo](python_logo.png)

## Overview

This project implements a custom random number generator that produces 5-digit integer random numbers. The generator is designed to pass various statistical tests, including Kolmogorov-Smirnov, Chi-Squared, Autocorrelation, and Poker tests. The goal is to create a custom random number generator that is comparable to Python's built-in `rand()` function.

## Algorithm

The custom random number generator follows these steps:

1. **Initialization**: The generator starts with an initial seed value.

2. **Geometric Time Events**: The generator captures geometric time events (e.g., CPU clock cycles or system time) to obtain time values.

3. **Transformation**: Time values are transformed using mathematical operations to create numerical sequences.

4. **Random Number Sets**: Numerical sequences are combined to generate sets of 5-digit random numbers.

5. **Statistical Tests**: The generator undergoes four statistical tests:
   - Kolmogorov-Smirnov Test
   - Chi-Squared Test
   - Autocorrelation Test
   - Poker Test

6. **Evaluation**: P-values from each test are compared against critical values (99% confidence) to determine if the generator passes.

## Why This Generator?

- Designed for 5-digit integer random numbers.
- Meets stringent statistical tests for randomness.
- Comparable to Python's `rand()` function.
- Customizable and extensible.

## How to Use

1. Clone this repository.
2. Install required dependencies (`numpy`, `scipy`).
3. Run `custom_random_generator.py`.
4. Review the test results and the generated random numbers.

## Test Results

The custom random number generator has been tested against the Kolmogorov-Smirnov, Chi-Squared, Autocorrelation, and Poker tests.

- Kolmogorov-Smirnov p-value: [Insert p-value]
- Chi-Squared p-value: [Insert p-value]
- Autocorrelation p-value: [Insert p-value]
- Poker Test Result: [Insert p-value]

## License

This project is licensed under the [MIT License](LICENSE).
