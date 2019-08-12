####
Try it Out - Array Manipulation 2
Now, Change the shape of x to (4, 5) and assign it to new array z.

Split the array z vertically in to two arrays.

Hint: Use vsplit
####

import numpy as np
x=np.arange(1,21)
print(x.shape)
y=x.reshape(2,10)
print(np.vsplit(y,2))
z=x.reshape(4,5)
print(np.vsplit(z,2))
