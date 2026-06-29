import numpy as np
class Solution:
    def matrixReshape(self, mat, r, c):
        mat = np.array(mat)
        if mat.size != r*c:
            return mat.tolist()
        return mat.reshape(r,c).tolist()
