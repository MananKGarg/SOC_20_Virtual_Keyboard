import numpy as np
import math

def mean_filter(arr, k):
  x = np.pad(arr, (k,k), 'constant', constant_values = (0,0))
  ret = np.cumsum(x, dtype = float)
  ret[(2*k+1):] = ret[(2*k+1):] - ret[:-(2*k+1)]
  return ret[2*k:]/(2*k+1)
  
  
def generate_sin_wave(period, range_, num):
  y = np.arange((2*math.pi*range_[0])/period, (2*math.pi*range_[1])/period, 2*math.pi*(range_[1]-range_[0])/(num*period))
  sin_values = np.sin(y)
  return sin_values
  
  
def noisify(array, var):
  noise = np.random.normal(0, math.sqrt(var), len(array))
  result = array + noise
  return result

