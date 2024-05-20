import numpy as np
#function to draw sample from the distribution
def drawSamples(pmf: dict[str, float], n: int) -> list[str]:
    sample1=[]
    c=0
    cdf=[]
    #generating cumulative function
    for i in pmf.values():
        c+=i
        cdf.append(c)
    X=[]
    #generating random uniformly distributed values
    for i in range(n):
        x=np.random.uniform(0,1)
        j = 0
        found = False
        while j < len(cdf) and not found:
            if x < cdf[j]:
                sample1.append(list(pmf.keys())[j])
                found = True
            j += 1
    return sample1
pmf = {'Apple': 0.5, 'Banana': 0.3, 'Carrot': 0.2}
n = 10
#passing the dictionary values,n and probablity values into random sampler functions
print(drawSamples(pmf,n))
