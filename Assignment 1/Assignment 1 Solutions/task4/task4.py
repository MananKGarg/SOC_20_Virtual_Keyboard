import numpy as np

def mean_filter(arr, k):
    kp = 2*k+1
    arr = np.pad(arr, k+1, mode='constant')
    p = np.cumsum(arr)
    return (p[kp:] - p[:-kp])[:-1] / kp

def generate_sin_wave(period, range_, num):
    x = np.linspace(*range_, num=num)
    y = np.sin(x * np.pi * 2 / period)
    return y.flatten()

def noisify(arr, var):
    arr = arr.copy()
    arr += np.random.randn(*arr.shape)*np.sqrt(var)
    return arr
