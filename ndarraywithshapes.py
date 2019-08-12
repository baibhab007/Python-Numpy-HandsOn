####
Try it Out - ndarray with Shapes
Import numpy package as np

Define a ndarray x2, whose shape is (3, 2, 2) and contains all 1's.

Define a ndarray x3, whose shape is (4,4) and contains 1's on diagonal and 0's elsewhere.
####

import numpy as np
x2 = np.ones(shape=(3,2,2))
x3 = np.eye(4,4)
print(x2)
print(x3)
