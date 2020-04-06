import numpy as np

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
