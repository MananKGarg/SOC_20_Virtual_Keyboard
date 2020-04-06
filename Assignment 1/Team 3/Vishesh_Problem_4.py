import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def mean_filter(a,k):
	
	l = len(a)
	b = np.zeros(l)
	k1 = a[k-1:0:-1]+[a[0]]		#[a[0]]*a[0]
	k2 = a[l:l-k-1:-1]		#[a[l-1]]*a[l-1]
	a_ = np.array(k1+a+k2)
	print(a_)
	b = list(map(lambda i:np.average(a_[i-k:i+k+1]),range(k,k+l)))
	print(b)


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


def noisify(array, var):
	return np.random.normal(0,var,1000)


noise=noisify(clean_sin,var)
dirty_sin=clean_sin+noise
