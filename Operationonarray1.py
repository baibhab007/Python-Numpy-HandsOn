####
Try it Out - Operations on Arrays 1
Create a 2-D array y of shape (2, 3), having numbers from 1 to 6.

Square each element of y.

Add 5 to each element of resulted array.
####

import numpy as np
y = np.arange(1,7).reshape(2,3)
print((y**2)+5)
