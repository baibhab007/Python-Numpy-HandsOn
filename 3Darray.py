####
Try it Out - 3D array
Define a random 3-D array x4 of shape (3, 4, 2) and of numbers between 0 and 1.

Simulate a random normal distribution of 20 elements, whose mean is 5 and standard deviation 2.5 . Capture the result in x5.
####

import numpy as np
x4 = np.random.rand(3,4,2)
x5 = 5 + 2.5*np.random.randn(20)
print(x4)
print(x5)
