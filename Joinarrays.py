####
Try it Out - Join Arrays
Create a 2-D array p, of shape (2, 2) with elements 3, 6, 9, 12.

Create a 2-D array q, of shape (2, 3) with elements 15, 18, 21, 24, 27, 30.

Join the two arrays p and q horizontally
####

import numpy as np
p=np.array([3,6,9,12]).reshape(2,2)
q=np.array([15,18,21,24,27,30]).reshape(2,3)
print(np.hstack((p,q)))
