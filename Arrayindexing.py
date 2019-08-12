####
Try it Out - Array Indexing
Create a array x of shape (6, 5), having first 30 natural numbers.

Obtain elements of last row.

Obtain elements of middle column.

Obtain elements, overlapping first two rows and last three columns.
####

import numpy as np
x = np.arange(1,31).reshape(6,5)
print(x)
print(x[5])
print(x[:,2])
