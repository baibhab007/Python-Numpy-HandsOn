####
Try it Out - Determine Attributes
Import numpy package as np.

Define the list of lists n = [[-1, -2, -3, -4], [-2,-4, -6, -8]].

Create a numpy array y, using array method of numpy package.

Hint : Pass list n as argument to array method.
Determine the type of array y.

Determine the following attributes.

Dimensions of y.

Shape of y.

Size of y.

Type of each data element of y.

Number of bytes occupied by each data element of y
####

import numpy as np
n = [[-1, -2, -3, -4], [-2,-4, -6, -8]]
y = np.array(n)
print(type(y))
print(y.ndim)
print(y.shape)
print(y.size)
print(y.dtype)
print(y.nbytes)
