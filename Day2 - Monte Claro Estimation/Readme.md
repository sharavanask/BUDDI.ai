# Monte Carlo Estimation of π using Uniform Distribution

This Python script estimates the value of π using the Monte Carlo method with a uniform distribution. The idea is to randomly throw darts into a square and count how many fall inside a quarter circle inscribed within the square. By comparing the ratio of darts inside the circle to the total darts thrown, multiplied by 4, we get an estimate of π.

## How It Works

- The script generates random points (x, y) within a square with side length 1.
- It checks if each point falls inside a quarter circle with radius 0.5 centered at the origin.
- The proportion of points inside the circle is used to estimate π.
- The process is repeated for different numbers of random points to observe how the estimation converges to π.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies using the following command:
   ```bash
   pip install numpy matplotlib
   ```
3. Run the script:
   ```bash
   python monte_carlo_pi.py
   ```

## Results

The script generates a plot showing how the estimated value of π converges as more random points are used in the simulation. The x-axis represents the number of darts thrown, and the y-axis represents the estimated value of π.

The Monte Carlo method provides a simple yet powerful way to approximate π and is widely used in computational mathematics and statistics.

## Visualization

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day2%20-%20Monte%20Claro%20Estimation/Screenshot%20from%202024-05-20%2010-17-29.png)

![Estimated PI](https://github.com/sharavanask/BUDDI.ai/blob/main/Day2%20-%20Monte%20Claro%20Estimation/Screenshot%20from%202024-05-20%2010-19-05.png)
