import numpy as np
from numpy.lib.stride_tricks import as_strided

def mean_filter(arr, k):
	n = len(arr)
	new  = np.empty([n+2*k])
	new[k:n+k] = arr[:]
	new[:k] = arr[::-1][-k:]
	new[n+k:n+2*k] = arr[::-1][:k]
	stride = new.strides[0]
	temp = as_strided(new, shape=(n,2*k+1), strides=(stride, stride))
	result = np.sum(temp, axis = 1)
	return result/(2*k+1)

def generate_sine_wave(period, range_, num):
	a = 2*np.pi/period
	x = np.linspace(range_[0], range_[1], num)
	return np.sin(a*x)

def noisify(array, var):
	result = array + np.random.normal(0, np.sqrt(var), len(array))
	return result