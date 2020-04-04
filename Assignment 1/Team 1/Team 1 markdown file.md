# Team Name
## Tagline

| Problem Number    | Team Member                                     |
| ----------------- | -----------                                     |
| Problem 1         |  [Aanal Sonara](https://github.com/Aanal2901)   |
| Problem 2         |  [Ankit Kumar Jain](https://github.com/akj0811) |
| Problem 3         |  [Aanal Sonara](https://github.com/Aanal2901)                                              |
| Problem 4         |  [Ankit Kumar Jain](https://github.com/akj0811) |


# 1. Aanal Sonara

## Problem 1:

 The problem is based on the statistics of cricket matches. We have to create a dictionary that contains the relevant info about players and their scores and a sorted list than contains the total score of a player across all matches.

## Requisites:

 * Dictionary
 * List

## Insights:

 * The match name and the match info is taken via the input stream as a continuous string.
 * The string is then splitted by certain delimiters to obtain the match name and the corresponding match info(that comprises the player names and their scores) using the **split()** function.
 * The overall match info of all the matches is then stored as a nested dictionary.
 * Then to obtain the list of the players and their total score across all matches, we store the player names and their scores in a dictionary. Whenever a player is already present in the dictionary, the score is added to it's value, else a new key is inserted. The dictionary is then converted to a list.
 * Finally the sorted score list (with respect to the decreasing scores followed by the player name in the lexicographically decreasing order) is obtained using the **sorted()** function.

## Code:

```python
n=int(input())
dict1={}
sub_dict1={}
import numpy as np
for i in range(n):
    data=input()
    data=data.split(":")
    data[1]=data[1].split(',')
    for j in range(len(data[1])):
        data[1][j]=data[1][j].split('-')
        sub_dict1[data[1][j][0]]=int(data[1][j][1])
        dict1[data[0]]=(sub_dict1)
    sub_dict1={}
print(dict1)

final_dict={}
for key, value in dict1.items():
    for player in value:
        if player in final_dict:
            final_dict[player] += value[player]
        else:
            final_dict[player] = value[player]
data =[('name', 'U10'),('score', int)]
final_list = np.array(list(final_dict.items()), dtype=data)
final_list[::-1].sort(order= ['score', 'name'])

print(final_list)
```

## Problem 3:

 The problem is based on Image Processing Teachnique and Machine Learning unsupervised learning algorithm K-clustering. In this algorithm the data n clusters are formed of the data. The clusters have a centroid. Thus for segmentation of image, the pixels are given the pxel value of the nearest centroid.
 
## Requisites 
 * Numpy Library
 * Matplot Library
 * PIL Library
 * Scipy Library
 
 ## Insights:
  
  * In the first input we have to give the path of the image. (preferable full path)
  * The second input is the number of clusters.
  * The image file is first converted into a 3D array. Each pixel value is a 3D vector. 
  * To pass it to Kmeans it is converted to a 2D array, where number of rows = total number of pixels, number of columns = 3, each row       representing a vector.
  * After it is passed into Kmeans, k clusters are formed. The returned values are
      * (k, 3) sized array, which contains value of all the centroids of all clusters.
      * 1D array of labels, which the cluster number (or centroid) that pixel is closest to.
  * The centroid array is converted to int and other pixels are given the values of closest centroid.
  * The small segmented array is reshaped to original array.
 ## Code:
 ```
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
```


# 2. Ankit Kumar Jain

## Problem 2:

 The problem is based on an Image Processing Technique which aims at filtering out the Salt and Pepper Noise. To filter out the noise, we undertake an algorithm that assigns a mean of the intensity values of a pixel across the various patches provided as an input. In this problem, we are simply asked to write down the function that implements it.

## Requisites:

 * Numpy Library

## Insights:

 * All the data is stored in a Numpy array.
 * All the intermediate arrays have been initialised to the required values.
 * While iterating over the patches, all these arrays have been modified using the **Numpy.where()** function that is basically a tool to avoid tedious **(if..else)** statemnets while iterating over the array elements.
 * Finally, for the processed array, the given conditions have been imposed appropriately.

## Code:

```python
import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
    white_count = np.zeros(shape)
    black_count = np.zeros(shape)
    mid_total = np.zeros(shape)
    mid_count = np.zeros(shape)
    for (r1, c1, r2, c2), x in input_dict.items():
        white_count[r1:r2, c1:c2] += np.where(x == 255, 1, 0)
        black_count[r1:r2, c1:c2] += np.where(x == 0, 1, 0)
        x = np.mod(x, 255)
        mid_count[r1:r2, c1:c2] += np.where(x == 0, 0, 1)
        mid_total[r1:r2, c1:c2] += x

    mid_count = np.where(mid_count == 0, 1, mid_count)
    mid_total = np.divide(mid_total, mid_count)
    M = np.where(mid_total == 0, 255*(white_count >= black_count), mid_total)
    a = mid_total+white_count+black_count
    M = np.where(a == 0, a, M)
    return M
```

## Problem 4:

 This problem requires us to write a few functions namely:
 * mean-filter - an image processing technique to remove some noise and smoothen the edges of an image.
 * sine wave function - it generates data set for plotting a sine wave.
 * Gaussian noise addition - To make the data more realistic in some sense.

## Requisites:

 * Numpy Library

## Insights:

 * mean-filter - numpy striding and array slicing is used to avoid **for** loops. Strides are really efficient because they jump into the memory locations directly.
 * sine wave function - numpy sin function is used to apply sine function to every element of the array without explicitly writing the **for** loop, **numpy.linspace()** has been used a generator of equi-spaced floating point numbers.
 * Gaussian noise addition - **numpy.random.normal()** has been used to generate random numbers from the normal distribution with specific variance and mean.

## Code:

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

def mean_filter(arr, k):
    n = len(arr)
    new  = np.empty([n+2*k])
    new[k:n+k] = arr[:]
    new[:k] = arr[::-1][-k:]
    new[n+k:n+2*k] = arr[::-1][:k]
    stride = new.strides[0]
    temp = as_strided(new, shape=(n,2*k+1), strides=(stride, stride))
    result = np.sum(temp, axis = 1)
    return result/(2*k+1)

def generate_sine_wave(period, range_, num):
    a = 2*np.pi/period
    x = np.linspace(range_[0], range_[1], num)
    return np.sin(a*x)

def noisify(array, var):
    result = array + np.random.normal(0, np.sqrt(var), len(array))
    return result
```

