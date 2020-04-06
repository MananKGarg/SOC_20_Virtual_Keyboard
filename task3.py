from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2


def solve(filepath, k):
    im = Image.open(filepath,'r')
    im = im.convert('RGB')
    width, height = im.size
  
    px_values = list(im.getdata())
    px_values = np.array(px_values)
    px_values = np.array(px_values).reshape(width*height, 3)
    px_values = px_values.astype(float)
   
    centroid, label = kmeans2(px_values, k, minit='++')
   
    for i in range(np.size(px_values, 0)):
        for j in range(3):
            px_values[i,j] = centroid[label[i],j]
            
    px_values_1 = np.zeros((width, height, 3))
    for i in range(3):
        px_values_1[:, :, i] = px_values[:, i].reshape(width, height)
    
    im2 = Image.fromarray(px_values_1, 'RGB')
    im2.show()
    im2.save(filepath)


def main():
    filepath = input("Enter path to image : ")
    k = ("Enter value of k : ")
    x = "r" + "\"" + filepath + "\""
    solve(x,k)
    
