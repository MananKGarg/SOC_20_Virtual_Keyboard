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
