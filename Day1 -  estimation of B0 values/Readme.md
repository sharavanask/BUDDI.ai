#
# Buddi.Ai Internship May-June 2024

A brief description of what this project does and who it's for

wdwfe
Code Explanation
Import Libraries:

numpy is imported for numerical operations.
matplotlib.pyplot is imported for plotting the 3D surface plot.
Data Initialization:

X and Y are numpy arrays representing the input data points and the corresponding output values.
Variable Initialization:

beta1 and beta2 are lists that will store the tested values of 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
 .
E is a list that will store the calculated error for each combination of 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
 .
MinEpsilon is initialized to a very large number to track the minimum error encountered.
B1 and B2 are initialized to -1 to store the 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
  values that result in the minimum error.
Grid Search:

A nested loop iterates over the range of -3 to 3 for both 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
 .
For each combination of 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
 :
Calculate the predicted value Val using the formula 
𝛽
1
𝑋
+
𝛽
2
𝑋
2
β 
1
​
 X+β 
2
​
 X 
2
 .
Calculate the sum of absolute errors between the predicted values and the actual values Y.
Append the current 
𝛽
1
β 
1
​
 , 
𝛽
2
β 
2
​
 , and error to their respective lists.
Update MinEpsilon, B1, and B2 if the current error is smaller than MinEpsilon.
Output:

Print the minimum error and the corresponding 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
  values.
Plotting:

Create a 3D surface plot using plot_trisurf to visualize the error as a function of 
𝛽
1
β 
1
​
  and 
𝛽
2
β 
2
​
 .
Set the labels for the axes and the title of the plot.
Display the plot using plt.show().
To run this script, make sure you have the necessary libraries installed and execute the script in your Python environment. The script will print the minimum error and the best parameters, and it will generate a 3D plot of the error surface.
[Variation of B0 and B1 values](Day1 -  estimation of B0 values/1.png)








