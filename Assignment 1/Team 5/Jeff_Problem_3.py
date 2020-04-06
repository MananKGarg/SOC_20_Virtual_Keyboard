import numpy as np
import scipy
from scipy.cluster.vq import kmeans2
from PIL import Image
from matplotlib import image
from matplotlib import pyplot

def make_cool(inp, k):
    image_array = np.array(Image.open(inp), np.float)                               #convert image to array
    image_array1 = image_array.reshape((-1,3))                                      #flatten the array
    
    centers, labels = kmeans2(image_array1, k, minit='++')                          #obtain kmeans centers and labels
    centers = np.uint8(centers)
    
    output_array = centers[labels].reshape(image_array.shape)                       #build our output array
    
    output = Image.fromarray(output_array, 'RGB')                                   #conver our array to an image
    output.save('pic1.png')                                                         #save our image
  
