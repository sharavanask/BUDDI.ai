import numpy as np
import math
import matplotlib.pyplot as plt
a=1
X=[]
Y=[]

n=[10,100,1000,10000,100000,1000000]

def incircle(a,b):
  if math.sqrt((a**2)+(b**2)) <= 0.5:
    return True
def check(n):
  PI=[]
  ans=0
  for i in range(n):
    x=np.random.normal(0,5)
    while(x>0.5 or x<-0.5):
      x=np.random.normal(0,5)
    X.append(x)
    y=np.random.normal(0,5)
    while(y>0.5 or y<-0.5):
      y=np.random.normal(0,5)
    if incircle(x,y):
      ans+=1
  return ans/n
v=[]
for i in n:
  d=check(i)
  v.append(d*4)
print(v)
plt.xscale("log")
plt.plot(n,v)
plt.xlabel("Darts")  
plt.ylabel("PI")  
plt.legend("PI")
plt.figtext(0,0.01,"Imagine a circle drawn inside a square. If you throw many darts randomly at the square, some will land inside the circle and some outside. By counting the proportion of darts that hit inside the circle compared to all the darts thrown,then multiplying this proportion by 4, you can get a good estimate of the number π",fontsize = 8)
#plt.text(1, 10, description, fontsize=10, ha='left', va='top', wrap=True, bbox=dict(facecolor='lightblue', alpha=0.5))
plt.axhline(y=3.14,color='black', linestyle="-")
plt.title(" Estimated PI using  Monte Claro usimg Normal Distribution")
plt.show()
