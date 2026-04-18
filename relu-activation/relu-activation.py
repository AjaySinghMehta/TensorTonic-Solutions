import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    arr = np.asarray(x)
    return np.maximum(0.0,arr)