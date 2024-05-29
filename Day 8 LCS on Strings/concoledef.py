import matplotlib.pyplot as plt
def convolve(S1, S2):
    #converting the strings into array
    s1 = list(S1.split(" "))
    s2 = list(S2.split(" "))
    #array to store substing output
    st = []
    #array to store exact substring output
    ex = []
    st1 = []
    ex1 = [] 
    #iterating the strings 
    for i in range(1, len(s1) + 1):
        s11 = s1[(len(s1) - i):]
        s22 = s2[:i]
        #variable to calculate backward convole
        ste = 0
        exe = 0#iterate the strings to check for substrings
        for j in range(len(s11)):
            if s22[j] in s11:
                ste += 1
            if s11[j] == s22[j]:
                exe += 1 
        st.append(ste)
        ex.append(exe)
        #backward convolution strings
        S11 = s1[:len(s1) - i]
        S22 = s2[i:]
        #calculating forward convole
        ste1 = 0
        exe1 = 0
        #iterating the functions to check for exact match
        for j in range(len(S11)):
            if S22[j] in S11:
                ste1 += 1
            if S11[j] == S22[j]:
                exe1 += 1 
        st1.append(ste1)
        ex1.append(exe1)
    #returning output of substring and exact  
    return st + st1, ex + ex1
#two strings as input
S1 = "he is a bad boy"
S2 = "i watch bad boy 2"
#functions to perform LCS on strings
S, E = convolve(S1, S2)
#printinh the outputs
print('String 1',S1)
print('Strng 2',S2)
print("Substring convolve:",S)
print("Exact convolve:",E)
#x coordinates for plotting
x=list(range(-len(S1.split()),len(S2.split())))
plt.plot(x,S,label="SUbstring LCS")
plt.plot(x,E,label="Exact LCS")
plt.xlabel('Position')
plt.ylabel('LCS')
plt.title('LCS algorithm on Strings')
plt.figtext(0.5, 0.01, "In the above graph the LCS algorithm is executed on Two different String and its output is plotted in two different types as checking in its substrings and at its exact position", ha="center", fontsize=10, bbox={"facecolor":"brown", "alpha":0.5, "pad":5})
plt.legend()
plt.show()
