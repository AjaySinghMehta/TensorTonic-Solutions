import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    arr = np.asarray(A)
    rows , cols = arr.shape
    ans = np.zeros((cols,rows))
    for i in range(rows):
        for j in range(cols):
            ans[j][i] = arr[i][j]
    return ans
    
        