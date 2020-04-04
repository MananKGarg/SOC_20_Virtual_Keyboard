# Team Name
## Tagline

| Problem Number    | Team Member                                     |
| ----------------- | -----------                                     |
| Problem 1         |  [Aanal Sonara](https://github.com/Aanal2901)   |
| Problem 2         |  [Ankit Kumar Jain](https://github.com/akj0811) |
| Problem 3         |                                                 |
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

final_list = []
for key in final_dict:
    final_list.append((key, final_dict[key]))
final_list=sorted(final_list, key=lambda x: x[1], reverse=True)

for i in range(len(final_list)-1):
    if final_list[i][1]==final_list[i+1][1]:
        if final_list[i][0]>final_list[i+1][0]:
            temp = final_list[i]
            final_list[i]=final_list[i+1]
            final_list[i+1]=temp
print(final_list)
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

