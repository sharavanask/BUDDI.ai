
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

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-20%2010-24-13.png)

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%205%20Legrange%2CBias%20Variance%20Polynomial%20model/Screenshot%20from%202024-05-20%2010-24-35.png)


