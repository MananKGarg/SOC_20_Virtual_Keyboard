import os, sys
from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2

input_file = Image.open(sys.argv[2],mode='r')
k = int(sys.argv[4])
output_file = open(sys.argv[6],'r+') 

size = input_file.size
input = input_file.load()
data = []
for x in range(size[0]):
	for y in range(size[1]):
		data.append(tuple(input[x,y]))
    
data = np.array(data)
data = data.astype('float64')	

centroid, label = kmeans2(data,k,minit='++')

np_label = np.array(label)
for x in np.unique(np_label):
	data[np_label==x] = centroid[x]

picture = Image.new("RGB",size)
data = data.astype('int64')
pic = picture.load()
print(data)
for x in range(size[0]):
	for y in range(size[1]):
		pic[x,y] = tuple(data[x*size[1]+y]) 

picture.save(output_file,'JPEG')


