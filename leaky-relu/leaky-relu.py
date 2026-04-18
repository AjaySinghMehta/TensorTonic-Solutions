import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    arr = np.asarray(x)
    # ans = []
    # for i in arr:
    #     if(i<0):
    #         ans.append(alpha*i)
    #     else:
    #         ans.append(i)
    # ans = np.asarray(ans)
    # return ans
    return np.where(arr>=0,arr,alpha*arr)
