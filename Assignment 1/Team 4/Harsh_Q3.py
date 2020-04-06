import argparse
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.cluster import vq

parser = argparse.ArgumentParser()  		#to read command line Arguments
parser.add_argument('--input')
parser.add_argument('--k', type=int)
parser.add_argument('--output')
args = parser.parse_args()

img = mpimg.imread(args.input).astype(float) 	# read the image as numpy array

img = img[:, :, :3]   				# trim the array , we need only RGB values

t = img <= 1 					#check whether the all the elements of array is < 1
if not np.all(t):
    img = img/255  				#if not divide by 255


(r, c, ch) = img.shape   
img1 = img.reshape(r*c, ch)			#reshape the array to 2D array

try:
	centroid, label = vq.kmeans2(img1, args.k, minit="++")
except Exception as e:
	centroid, label = vq.kmeans2(img1, args.k)  #when minit="++" is not appropriate for the given inputs

img1 = centroid[label]
img1 = img1.reshape(r, c, 3)
plt.imshow(img1)  				# create image from the array
plt.savefig(args.output)			#save the image at the desired place
# plt.show()
