####
Try it Out - Array Manipulation 1
Create a ndarray x having first 20 natural numbers, using arange method.

Determine the shape of x.

Change the shape of x to (2, 10) and assign it to new array y.

Split the array y horizontally in to two arrays.
####

import numpy as np
x=np.arange(1,21)
print(x.shape)
y=x.reshape(2,10)
print(np.vsplit(y,2))
