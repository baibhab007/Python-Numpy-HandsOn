####
Try it Out - Array Creation
Write the statement to import numpy package as np.

Define the list n = [5, 10, 15, 20, 25].

Create a numpy array x, using array method of numpy package.

Hint : Pass list n as argument to array method.
Determine the type of array x.

Determine the following attributes.

Dimensions of x.

Shape of x.

Size of x.
####

import numpy as np
n = [5, 10, 15, 20, 25]
x = np.array(n)
print(type(x))
print(x.ndim)
print(x.shape)
print(x.size)
