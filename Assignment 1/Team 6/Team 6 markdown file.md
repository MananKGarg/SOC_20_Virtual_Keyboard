TeamName
---

> Tagline(Yet to do decided)

|Problem Number | Team Member |
| --------- | --------------- |
| Problem 1 | [Rushil Koppaka]() |
| Problem 2 | [Akshat Vira](https://github.com/ViraAkshat) |
| Problem 3 | [Devansh Saini]() |
| Problem 4 | [Riya Agrawal]() |



# 1. Rushil Koppaka

 ## Problem
 - Put the description here

## Solution

```python
match_name_list=[]                                          #initialising lists
match_list=[]
final_player_names=[]
final_scores=[]

a=int(input('enter no.of matches:'))
for i in range(0,a):                                                 #getting main dictionary(entire league)
    match_name=input('enter match name:')
    match_name_list.append(match_name)
    single_match_dict = {}
    while True:                                           #getting inside dictionary(individual match)
        check=input('to go next match type no else press enter\n')
        if check=='no':
            print()
            break
        else:
            player_name,runs_scored=input('player name:'),int(input('runs scored:'))
            single_match_dict[player_name]=runs_scored
            if player_name in final_player_names:                                             #for tuple scorecard incrementing score of individual
                final_scores[final_player_names.index(player_name)]+=runs_scored
            else:
                final_player_names.append(player_name)
                final_scores.append(runs_scored)

    match_list.append(single_match_dict)

final_dict=dict(zip(match_name_list,match_list))
print(final_dict)

scorecard=list(zip(final_player_names,final_scores))                #creating tuple list

s=sorted(scorecard,reverse=True)                                    #sorting names in decreasing lexicographic order
s2=sorted(s,key= lambda x:x[1],reverse=True)                        #sorting according to runs scored

print(s2)



```

# 2. Akshat Vira
 
 ## Problem
 - The problem requires us to reconstruct an image based on information of its patches whilst minimising the noise while reconstructing the image.

- Images often contain various noises, Salt & Pepper noise is one such noise. Due to this noise, some pixels get corrupted with a certain probability, into either black or white.

- This can be achieved by following an algorithm and applying it to each pixel location of image.

- The task is to create a function which uses this algorithm and thereby reconstructs the image.

## Solution

```python
import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict:
    key: 4-tuple: (tlr, tlc, brr, brc):
            location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are evclusive.
            i.e. if M is the reconstructed matriv. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.
    value: 2d numpy array: the image patch.
    shape: shape of the original matrix.
    """

    black_count, white_count, mid_count, mid_total = np.zeros(shape), np.zeros(shape), np.zeros(shape), np.zeros(shape)
    M = np.zeros(shape)

    for tup, val in input_dict.items():
        tlr, tlc, brr, brc = tup
        white_count[tlr:brr, tlc:brc] += np.where(val == 255, 1, 0)
        black_count[tlr:brr, tlc:brc] += np.where(val == 0, 1, 0)
        mid_count[tlr:brr, tlc:brc] += np.where(np.logical_and(val != 0, val != 255), 1, 0)
        val = np.mod(val, 255)
        mid_total[tlr:brr, tlc:brc] += val

    #if mid_count != 0 final value is total/count
    #mid_total = np.where(mid_count == 0, mid_total, np.divide(mid_total, mid_count))
    mid_total = np.divide(mid_total, mid_count + (mid_count == 0))
    #if mid_count is 0 & white>black put 255 else put 0
    mid_total = np.where(mid_count == 0, np.where(white_count >= black_count, 255, 0), mid_total)

    #if no patch then put 0
    M = np.where(mid_count + white_count + black_count == 0, 0, mid_total)

    return M
```


# 3. Devansh Saini
 
 ## Problem
- Put the description here

## Solution

```python

```


# 4. Riya Agrawal
 
 ## Problem
- Put the description here

## Solution

```python
import numpy as np
import math

def mean_filter(arr, k):
  x = np.pad(arr, (k,k), 'constant', constant_values = (0,0))
  ret = np.cumsum(x, dtype = float)
  ret[(2*k+1):] = ret[(2*k+1):] - ret[:-(2*k+1)]
  return ret[2*k:]/(2*k+1)
  
  
def generate_sin_wave(period, range_, num):
  y = np.arange((2*math.pi*range_[0])/period, (2*math.pi*range_[1])/period, 2*math.pi*(range_[1]-range_[0])/(num*period))
  sin_values = np.sin(y)
  return sin_values
  
  
def noisify(array, var):
  noise = np.random.normal(0, math.sqrt(var), len(array))
  result = array + noise
  return result



```
