from task4 import mean_filter, generate_sin_wave, noisify
import matplotlib.pyplot as plt

clean_sin = generate_sin_wave(2, (-2,8), 1000)
plt.plot(clean_sin)
plt.show() 
f,ax = plt.subplots()
ax.plot(clean_sin)
plt.savefig("clean_sin")
plt.show() 

dirty_sin = noisify(clean_sin, 0.05**2)
plt.plot(dirty_sin)
plt.show()
f,ax = plt.subplots()
ax.plot(dirty_sin)
plt.savefig("dirty_sin")
plt.show()

cleaned_sin = mean_filter(dirty_sin, 1)
plt.plot(cleaned_sin)
plt.show()
f, ax = plt.subplots()
ax.plot(cleaned_sin)
plt.savefig("cleaned_sin")
plt.show()
