# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
path=input()
#'C:\\Users\\TEMP\\Downloads\\pic1.jpg'
img = np.array(Image.open(path), np.float)

a = [[[] for i in range(3)] for j in range(img.shape[0]*img.shape[1])]

a =np.reshape(img, (img.shape[0]*img.shape[1], 3))

k = int(input())
from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
(centers), labels = kmeans2(a, k, minit='++')

#print(img)

centers = np.uint8(centers)
labels =labels.flatten()
seg_img = centers[labels]

seg_img = np.reshape(seg_img, img.shape)
print(seg_img.shape)
Image.open()

plt.imshow(seg_img)
plt.show()