# Monte Carlo Sampling from Probability Mass Function (PMF)

This Python script provides a function to draw samples from a given probability mass function (PMF) using a Monte Carlo method. The PMF represents the probabilities of different outcomes, and the Monte Carlo method simulates random sampling based on these probabilities.

## How It Works

The `drawSamples` function takes two inputs:
- `pmf`: A dictionary containing the outcomes as keys and their respective probabilities as values.
- `n`: The number of samples to draw from the PMF.

The function generates random samples by simulating a uniform distribution between 0 and 1. It uses the cumulative probabilities derived from the PMF to determine which outcome each random sample corresponds to.

## Usage

1. Define your PMF as a Python dictionary where keys are outcomes and values are their probabilities.
2. Call the `drawSamples` function with the PMF dictionary and the number of samples (`n`).

Example usage:
```python
import numpy as np

def drawSamples(pmf: dict[str, float], n: int) -> list[str]:
    # Function definition here...

pmf = {'Apple': 0.5, 'Banana': 0.3, 'Carrot': 0.2}
n = 10
samples = drawSamples(pmf, n)
print(samples)
```

## Requirements

- Python 3.x
- NumPy

## Function Description

### `drawSamples(pmf: dict[str, float], n: int) -> list[str]`
- `pmf`: A dictionary representing the Probability Mass Function (PMF) where keys are outcomes and values are probabilities.
- `n`: The number of samples to draw from the PMF.
- Returns a list of sampled outcomes based on the PMF probabilities.

## Results

The function returns a list of sampled outcomes based on the probabilities specified in the PMF. The number of samples (`n`) determines the size of the sample set.

## Example Output

For the provided PMF:
```python
pmf = {'Apple': 0.5, 'Banana': 0.3, 'Carrot': 0.2}
n = 10
```
The output may look like:
```
['Apple', 'Banana', 'Apple', 'Carrot', 'Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Carrot']
```

## Notes

- Ensure the probabilities in the PMF dictionary sum up to 1.
- The function uses NumPy for generating random samples.

---

This README provides an overview of the Monte Carlo sampling function, how to use it, function description, example usage, and expected output. Adjust the example output and description as needed based on your specific PMF and use case.
