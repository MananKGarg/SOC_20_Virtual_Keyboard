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

generate_sin_wave(period,range_,num)




print(clean_sin)

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
cleared_sin=mean_filter(dirty_sin,1)
plt.plot(x,cleared_sin,color = 'red', marker = "o")  
plt.title("cleared_sin")  
plt.xlabel("X")  
plt.ylabel("Y")  
plt.show() 
