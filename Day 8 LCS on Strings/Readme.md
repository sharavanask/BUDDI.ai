# Convolution of Strings 

## Longest Common Substring (LCS) Convolution and Visualization

This project implements a simple convolution algorithm to find the longest common substring (LCS) and exact matches between two input strings. The results are then visualized using a line plot to show the convolution of substrings and exact matches over different positions in the input strings.

### Files

- `convolve.py`: This script contains the main function to perform the convolution and visualize the results using Matplotlib.
- `README.md`: This file provides an overview and instructions for running the script.

### Requirements

- Python 3.x
- Matplotlib (for plotting)


# Function Explanation
convolve(S1, S2)
This function takes two input strings, S1 and S2, and performs the following steps:

Splits the strings into words.
Iterates through the strings to calculate the backward and forward convolutions.
Calculates the substring matches and exact matches.
Returns two lists: one for the substring matches and one for the exact matches.

# PLot showing the output 
![LCS](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%208%20LCS%20on%20Strings/string.png)

# Output
![output](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%208%20LCS%20on%20Strings/stringout.png)
