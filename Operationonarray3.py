####
Try it Out - Operation on Arrays 3
Create a array x of shape (50, ), having 50 random numbers from a normal distribution of mean 10 and standard deviation 2.

Calculate mean of x

Calculate Standard deviation of x

Calculate variance of x
####


import numpy as np
x = (10 + 2*np.random.randn(50)).reshape(50,)
print(x)
print(x.mean())
print(x.std())
print(x.var())
