# Team Name
## Tagline

| Problem Number    |                   Team Member                   |
| ----------------- | ----------------------------------------------- |
| Problem 1         |  [Aanal Sonara](https://github.com/Aanal2901)   |
| Problem 2         |  [Ankit Kumar Jain](https://github.com/akj0811) |
| Problem 3         |  [Aanal Sonara](https://github.com/Aanal2901)   |
| Problem 4         |  [Ankit Kumar Jain](https://github.com/akj0811) |


# 1. Aanal Sonara

## Problem 1:

 The problem is based on the statistics of cricket matches. We have to create a dictionary that contains the relevant info about players and their scores and a sorted list than contains the total score of a player across all matches.

## Requisites:

 * [Dictionary](https://www.geeksforgeeks.org/python-dictionary/)
 * [List](https://www.geeksforgeeks.org/python-list/)
 * [String](https://www.geeksforgeeks.org/python-strings/)

## Insights:

 * The match name and the match info is taken via the input stream as a continuous string.
 * The string is then splitted by certain delimiters to obtain the match name and the corresponding match info(that comprises the player names and their scores) using the **[split()](https://www.geeksforgeeks.org/python-string-split/)** function.
 * The overall match info of all the matches is then stored as a nested dictionary.
 * Then to obtain the list of the players and their total score across all matches, player names and their scores are stored in a dictionary. Whenever a key(player) is already present in the dictionary, the score is added to the corresponding value, else a new key is inserted. The dictionary is then converted to a list.
 * Finally the sorted score list (with respect to the decreasing scores and then by the player name in the lexicographically decreasing order) is obtained using the **[sorted()](https://www.geeksforgeeks.org/sorted-function-python/)** function.

## Code:

```python
import numpy as np

n=int(input())
dict1={}
final_dict={}
for i in range(n):
    data=input()
    sub_dict1={}
    data=data.split(":")
    data[1]=data[1].split(',')
    for j in range(len(data[1])):
        data[1][j]=data[1][j].split('-')
        sub_dict1[data[1][j][0]]=int(data[1][j][1])
        dict1[data[0]]=(sub_dict1)
        if data[1][j][0] in final_dict:
            final_dict[data[1][j][0]] += int(data[1][j][1])
        else:
            final_dict[data[1][j][0]] = int(data[1][j][1])
print(dict1)

data =[('name', 'U10'),('score', int)]
final_list = np.array(list(final_dict.items()), dtype=data)
final_list[::-1].sort(order= ['score', 'name'])

print(final_list)
```

## Problem 3:

 The problem is based on an Image Processing and Machine Learning - Unsupervised learning algorithm K Means Clustering. In this algorithm, **k** clusters are formed out of the data. Each cluster has it's own centroid. For segmentation of the image, the pixels are assigned the pixel value of the nearest (minimum Euclidean Distance) centroid.
 
## Requisites 
 * [Numpy Library](https://numpy.org/devdocs/user/quickstart.html)
 * [PIL Library](https://pillow.readthedocs.io/en/stable/)
 * [Scipy Library](https://scipy-lectures.org/intro/scipy.html)
 
## Insights:
  
 * The path of the image is given as an input. (preferably the full path)
 * The number of clusters is the second input.
 * The image file is first converted into a 3D array. Each pixel value is a 3D vector of RGB values.
 * To pass it to Kmeans++ function as an argument, it is converted to a 2D array of shape (total number of pixels, 3) where each row represents a vector of RGB values.
 * **[kmeans++](https://www.geeksforgeeks.org/ml-k-means-algorithm/)** forms **k** clusters out of the data. The return values of the function are - 
    * (k, 3) sized array, which contains pixel value of the centroid of all the clusters.
    * 1D array of labels, which gives the index of the centroid the pixel is closest to.
 * The centroid array is then typecasted to **int** and other pixels are given the pixel values of closest centroid.
 * The small segmented array is reshaped to original array using the **[reshape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)** function.
 * The final image is then generated from the resulting array using the **[fromarray](https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image)** function.

## Code:

```python
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
```


# 2. Ankit Kumar Jain

## Problem 2:

 The problem is based on an Image Processing Technique which aims at filtering out the Salt and Pepper Noise. To filter out the noise, we undertake an algorithm that assigns a mean of the intensity values of a pixel across the various patches provided as input. In this problem, we are simply asked to write down the function that implements it.

## Requisites:

 * [Numpy Library](https://numpy.org/devdocs/user/quickstart.html)

## Insights:

 * All the data is stored in a Numpy array.
 * All the intermediate arrays are initialised to the required values.
 * While iterating over the patches, all these arrays are modified using the **[Numpy.where()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html)** function that is basically a tool to avoid tedious **(if..else)** statemnets while iterating over the array elements.
 * Finally, for the processed array, the given conditions are imposed appropriately.

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

 This problem requires us to write a few functions, namely:
 * mean-filter - an image processing technique to remove some noise and smoothen the edges of an image.
 * sine wave function - it generates data set for plotting a sine wave.
 * Gaussian noise addition - to make the data more realistic in some sense.

## Requisites:

 * [Numpy Library](https://numpy.org/devdocs/user/quickstart.html)

## Insights:

 * mean-filter - numpy **[stride tricks](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.lib.stride_tricks.as_strided.html)** and **[array slicing](https://stackoverflow.com/questions/509211/understanding-slice-notation)** is used to avoid **for** loops. Strides are really efficient because they jump into the memory locations directly.
 * sine wave function - numpy sin function is used to apply sine function to every element of the array without explicitly writing the **for** loop, **[numpy.linspace()](https://www.geeksforgeeks.org/numpy-linspace-python/)** has been used a generator of equi-spaced floating point numbers.
 * Gaussian noise addition - **[numpy.random.normal()](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html)** is used to generate random numbers from the normal distribution with specific variance and mean.

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


