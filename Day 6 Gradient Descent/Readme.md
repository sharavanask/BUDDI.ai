# Gradient Descent for Linear Regression

This Python script implements gradient descent for linear regression and evaluates the model on both training and testing data. It utilizes NumPy for computation, Matplotlib for visualization, and scikit-learn for splitting the data into training and testing sets.

## Description

The script defines a function `gradient_descent` that performs gradient descent to optimize the coefficients of a linear regression model. It splits the data into training and testing sets, runs gradient descent on the training data, and evaluates the model's performance on the testing data.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn

You can install the required packages using pip:

```bash
pip install numpy matplotlib scikit-learn
```

## Usage

1. Clone the repository or download the Python script.
2. Make sure you have Python and the required packages installed.
3. Run the script using Python:
   ```bash
   python gradient_descent_linear_regression.py
   ```

## Function Description

### `gradient_descent(x, y, lr=0.01, tolerance=10e-6) -> (float, float, list, list, list, list)`
- `x`: Array of input features.
- `y`: Array of target values.
- `lr`: Learning rate for gradient descent (default is 0.01).
- `tolerance`: Convergence tolerance for stopping criterion (default is 10e-6).
- Returns:
  - `b0`: Final coefficient for the intercept.
  - `b1`: Final coefficient for the slope.
  - `E`: List of errors at each epoch.
  - `Epoch`: List of epoch numbers.
  - `Gb0`: List of coefficient values for intercept at each epoch.
  - `Gb1`: List of coefficient values for slope at each epoch.

## Example Output

```python
Gradient Descent training: b0: -2.957921573122759 b1: 1.9973980756436498
Final Training Error: 24.187102709780483
Gradient Descent testing: b0: -2.903180256889467 b1: 1.9990876792635678
Final Testing Error: 21.636235831554275
Test Error: 21.636235831554275
```

## Plot
![Gradient descent](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%206%20Gradient%20Descent/STOCHASTIC.png)


The plot shows the Mean Squared Error (MSE) with respect to the number of Epoch cycles for both training and testing data.






Here's a README.md template for your Python script that implements Stochastic Gradient Descent (SGD) for linear regression:

---

# Stochastic Gradient Descent (SGD) for Linear Regression

This Python script demonstrates Stochastic Gradient Descent (SGD) for linear regression. It uses NumPy for computation, Matplotlib for visualization, and scikit-learn for data splitting.

## Description

The script performs Stochastic Gradient Descent to optimize the coefficients of a linear regression model. It splits the data into training and testing sets using scikit-learn's `train_test_split` function and then applies SGD to train the model on the training data. The performance of the model is evaluated on both the training and testing data.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn

You can install the required packages using pip:

```bash
pip install numpy matplotlib scikit-learn
```

## Usage

1. Clone the repository or download the Python script.
2. Make sure you have Python and the required packages installed.
3. Run the script using Python:
   ```bash
   python stochastic_gradient_descent.py
   ```

## Function Description

### `stochasticdescent(x, y) -> (list, list, list, list)`
- `x`: Array of input features.
- `y`: Array of target values.
- Returns:
  - `Gb0`: List of beta0 values during training.
  - `Gb1`: List of beta1 values during training.
  - `E`: List of errors at each epoch.
  - `Epoch`: List of epoch numbers.

## Example Output

```
Gradient Descent training: b0: -2.957921573122759 b1: 1.9973980756436498
Final Training Error: 24.187102709780483
Gradient Descent testing: b0: -2.903180256889467 b1: 1.9990876792635678
Final Testing Error: 21.636235831554275
```
## Plot

![SGD](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%206%20Gradient%20Descent/GRADIENT.png)



The plot shows the Mean Squared Error (MSE) with respect to the number of Epoch cycles for both training and testing data.






# Minibatch Gradient Descent for Linear Regression

This Python script demonstrates minibatch gradient descent for linear regression. It uses NumPy for computation, Matplotlib for visualization, and scikit-learn for data splitting.

## Description

The script defines a function `minibatch_gradient_descent` that performs minibatch gradient descent to optimize the coefficients of a linear regression model. It splits the data into training and testing sets using scikit-learn's `train_test_split` function and then applies minibatch gradient descent to train the model on the training data. The performance of the model is evaluated on both the training and testing data.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn

You can install the required packages using pip:

```bash
pip install numpy matplotlib scikit-learn
```

## Usage

1. Clone the repository or download the Python script.
2. Make sure you have Python and the required packages installed.
3. Run the script using Python:
   ```bash
   python minibatch_gradient_descent.py
   ```

## Function Description

### `minibatch_gradient_descent(x, y, lr=0.01, tolerance=10e-6, num_minibatches=20) -> (float, float, list, list)`
- `x`: Array of input features.
- `y`: Array of target values.
- `lr`: Learning rate for minibatch gradient descent (default is 0.01).
- `tolerance`: Convergence tolerance for stopping criterion (default is 10e-6).
- `num_minibatches`: Number of minibatches to split the data into (default is 20).
- Returns:
  - `b0`: Final coefficient for the intercept.
  - `b1`: Final coefficient for the slope.
  - `E`: List of errors at each epoch.
  - `Epoch`: List of epoch numbers.

## Example Output

```
Minibatch Gradient Descent: b0: -2.957921573122759 b1: 1.9973980756436498 Final Error: 24.187102709780483
```

## Plot

![Minibatch Gradient Descent](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%206%20Gradient%20Descent/minibATCH.png)

![Minibatch Gradient Descent ](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%206%20Gradient%20Descent/Screenshot%20from%202024-05-20%2014-56-46.png)


The plot shows the Mean Squared Error (MSE) with respect to the number of Epoch cycles for both training and testing data.


