from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2

path = input()
k = int(input())

img = np.array(Image.open(path), np.float)
a = np.reshape(img, (-1, 3))
centers, labels = kmeans2(a, k, minit='++')

centers = np.uint8(centers)

seg_img = centers[labels]
seg_img = np.reshape(seg_img, img.shape)

new_img = Image.fromarray(seg_img, 'RGB')
new_img.save('new1.png')
