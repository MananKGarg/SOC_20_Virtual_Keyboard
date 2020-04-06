import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

range_=(-2,8)
num=1000
period=2
mean=0
var=0.05
x=[]
clean_sin=[]
dirty_sin=[]

def generate_sin_wave(period, range_,num):
	a=range_[0]
	b=range_[1]
	d=(b-a)/(num-1)
	i=1
	while (i<=num):
		p= a+ (i-1)*d
		q=math.sin(6.28*p/period)
		x.append(p)
		clean_sin.append(q)
		i=i+1

	return x,clean_sin


def noisify(array, var):
	return np.random.normal(0,var,1000)

	
generate_sin_wave(period,range_,num)


noise=noisify(clean_sin,var)
dirty_sin=clean_sin+noise


print(clean_sin)
print(noise)
print(dirty_sin)


plt.plot(x,clean_sin,color = 'red', marker = "o")  
plt.title("clean sin")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show()  

plt.plot(x,dirty_sin,color = 'red', marker = "o")  
plt.title("dirty_sin")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show() 
