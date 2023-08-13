
# # Custom Random Number Generator <br/>[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://pypi.org/project/numpy/) [![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)](https://pypi.org/project/scipy/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](https://pypi.org/project/matplotlib/) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Installations

* **Python 3** can be downloaded from [here](https://www.python.org/downloads/). Make sure to check **Add Python 3.x to PATH** during installation.
* **NumPy**, **SciPy**, and **matplotlib** **etc** libraries can be downloaded and installed using the commands:
```bash
pip install numpy
pip install scipy
pip install matplotlib
pip install library-name
```
or if you have multiple python version installed use this
```bash
py -3.9 -m pip install numpy
py -3.11 -m pip install numpy
.....
```
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
