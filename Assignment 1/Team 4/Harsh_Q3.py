import argparse
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.cluster import vq

parser = argparse.ArgumentParser()
parser.add_argument('--input')
parser.add_argument('--k', type=int)
parser.add_argument('--output')
args = parser.parse_args()

img = mpimg.imread(args.input).astype(float)

img = img[:, :, :3]

t = img <= 1
if not np.all(t):
    img = img/255


(r, c, ch) = img.shape
img1 = img.reshape(r*c, ch)

try:
	centroid, label = vq.kmeans2(img1, args.k, minit="++")
except Exception as e:
	centroid, label = vq.kmeans2(img1, args.k)

img1 = centroid[label]
img1 = img1.reshape(r, c, 3)
plt.imshow(img1)
plt.savefig(args.output)
# plt.show()