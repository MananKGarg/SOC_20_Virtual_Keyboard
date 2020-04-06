import matplotlib.pyplot as plt 
import numpy as np
from trial import generate_sine_wave, noisify, mean_filter
  
x = np.arange(-2, 8, 0.01)
clean_sin = generate_sine_wave(2, [-2,8], 1000)
dirty_sin = noisify(clean_sin, 0.05)
cleaned_sin = mean_filter(dirty_sin, 1)
plt.plot(x, dirty_sin) 
plt.plot(x, cleaned_sin)
plt.plot(x, clean_sin)
plt.show() 