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


def mean_filter(a,k):
	
	l = len(a)
	b = np.zeros(l) # Creates an array with all 0's of length of given array
	k1 = a[k-1:0:-1]+[a[0]]	# Creates a reflection of elements of a for average at edges	#[a[0]]*a[0]
	k2 = a[l:l-k-1:-1]	# Same as above	#[a[l-1]]*a[l-1]
	a_ = np.array(k1+a+k2) # If a=[1,2,3,4] with k=2 then a_ = [2,1,1,2,3,4,4,3]
	b = np.around(list(map(lambda i:np.average(a_[i-k:i+k+1]),range(k,k+l))),1) 
	# Creates an array with each element as average of k elements around it
	# for ex: a=[1,2,3,4] with k=2 returns [ 1.8  2.2  3.   4.   5.   6.   7.   7.8  8.2]
	return b


# mean_filter([1,2,3,4,5,6,7,8,9],2)

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


generate_sin_wave(period,range_,num)
def noisify(array, var):
	return (array+np.random.normal(0,var,1000))


dirty_sin=noisify(clean_sin,var)
