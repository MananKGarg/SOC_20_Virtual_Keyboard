# Team Name
## Tagline

| Problem Number    | Team Member |
| ----------------- | ----------- |
| Problem 1         |             |
| Problem 2         |             |
| Problem 3         |             |
| Problem 4         |             |


# 1. Aanal Sonara

## Problem 1:

##### The question is based on a statistics of various cricket matches. We have to then create a dictionary that contains the relevant players and their scores and a list than contains the total score of a player across all matches.

## Requisites:

##### * Dictionary
##### * List

## Code Insights:

##### * The data is stored in the string format.
##### * It is then splitted first between matches,then players. 
##### * It is then stored in a nested dictionary with player name and the corresponding score.
##### * To print the list of players and their total score I made a dictionary with players and their score, if the player name repeated, i added it's score to the original player score in dictionary. Then i converted it to a list.
##### * Finally the sorted score list (with respect to the scores and then the player name in the lexicographically decreasing order) is obtained.

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

##### The problem is some sort of an Image Processing Technique known which aims at filtering out the Salt and Pepper Noise. Here, we have to undertake a simple manipulative approach in which we simply take the mean of the pixel values across various patches and under certain conditions to try and filter out the noise. In this problem, we are simply asked to write down the function that implements it.

## Requisites:

##### * Numpy Library

## Code Insights:

##### * All the data is stored in an array. 
##### * All the intermediate arrays have been initialised to the required values.
##### * While iterating over the patches, all these arrays have been modified using the Numpy.where() function that is basically a tool to avoid tedious if..else condtions iterating over the array elements.
##### * Finally, for the processed array, the given conditions have been imposed appropriately.

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
