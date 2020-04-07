import matplotlib.pyplot as plt 
import numpy as np
from task4 import generate_sine_wave, noisify, mean_filter
  
x_data = np.arange(-2, 8, 0.01)

clean_sin = generate_sine_wave(2, [-2,8], 1000)
plt.plot(x_data, clean_sin)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sine Function')
plt.savefig('clean_sin.png')
plt.show()

dirty_sin = noisify(clean_sin, 0.05**2)
plt.plot(x_data, dirty_sin)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Noisy Sine Function!')
plt.savefig('dirty_sin.png')
plt.show()

cleaned_sin = mean_filter(dirty_sin, 1)
plt.plot(x_data, cleaned_sin)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Filtered Sine Function')
plt.savefig('cleaned_sin.png')
plt.show()
