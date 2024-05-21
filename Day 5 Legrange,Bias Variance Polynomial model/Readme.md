
# Lagrange Interpolation Polynomial

This Python script implements Lagrange interpolation to approximate a polynomial that passes through a given set of data points. It then visualizes the original data points and the interpolated polynomial using Matplotlib.

## Description

The script defines a function `lagrangeInterpolation` that takes arrays of x and y coordinates representing data points, along with an array of x values to interpolate, and computes the interpolated y values using Lagrange interpolation. It then plots the original data points and the interpolated polynomial.

## Usage

1. Clone the repository or download the Python script.
2. Ensure you have Python and Matplotlib installed.
3. Run the script using Python:
   ```bash
   python lagrange_interpolation.py
   ```
4. The script will generate a plot showing the known data points in blue dots and the Lagrange interpolation polynomial in red.

## Function Description

### `lagrangeInterpolation(x, y, xInterp) -> np.array`
- `x`: Array of x coordinates of known data points.
- `y`: Array of y coordinates of known data points.
- `xInterp`: Array of x values to interpolate.
- Returns an array of interpolated y values corresponding to `xInterp`.

## Example Plot
![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-20%2010-21-25.png)

# Polynomial Regression and Lagrange Interpolation

This project demonstrates polynomial regression (linear, quadratic, cubic, and biquadratic models) and Lagrange interpolation using a synthetic dataset. The code generates data points, fits polynomial models, and compares their performance through bias-variance tradeoff.

## Description

The script performs the following steps:
1. Generates synthetic data points based on a biquadratic polynomial with added noise.
2. Fits polynomial models of varying degrees (linear, quadratic, cubic, and biquadratic) to the data.
3. Uses Lagrange interpolation to approximate the function for a subset of the data.
4. Plots the fitted models and the interpolation.
5. Analyzes the bias-variance tradeoff by comparing the training and test errors for different model complexities.

## Dependencies

- `numpy`: For numerical operations.
- `matplotlib`: For plotting graphs.
- `random`: For generating random noise.

## Plot of different models and its bias variance upto biquadratic models

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-20%2010-24-13.png)

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-20%2010-24-35.png)

## Plot of different models and its bias variance upto decic Polynomial models

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/10.png)

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-21%2011-35-40.png)



