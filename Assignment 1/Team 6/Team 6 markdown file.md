Optimize Prime
---

> You light my fire(wall)

|Problem Number | Team Member |
| --------- | --------------- |
| Problem 1 | [Rushil Koppaka](https://github.com/rushilkoppaka) |
| Problem 2 | [Akshat Vira](https://github.com/ViraAkshat) |
| Problem 3 | [Devansh Saini]() |
| Problem 4 | [Riya Agrawal]() |



# 1. Rushil Koppaka

 ## Problem
 - The problem is based on the use of lists and dictionaries in python
 - The objective of the Question is to create a league table in the form of a dictionary which displays a particular match and the runs scored by people in that match.
 - It also asks us to display a list of tuples containing the amount of runs scored by each player in the entire tournament in a descending order based on runs scored.

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
- Images often contain various noises, Salt & Pepper noise is one such noise. Due to this noise, some pixels get corrupted with a certain probability, into either black or white.

- The problem requires us to reconstruct an image based on information of its patches whilst minimising the noise while reconstructing the image.

- This can be achieved by following an algorithm and applying it to each pixel location of image.

- The task is to create a function which uses this algorithm and thereby reconstructs the image.

## Solution

```python
import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict:
    key: 4-tuple: (tlr, tlc, brr, brc):
            location of the patch in the original image. tlr, tlc are inclusive but brr, brc are exclusive.
            i.e. if M is the reconstructed matrix. M[tlr:brr, tlc:brc] will give the patch.
    value: 2d numpy array: the image patch.
    shape: shape of the original matrix.
    """

    black_count, white_count = np.zeros(shape), np.zeros(shape)
    mid_count, mid_total = np.zeros(shape), np.zeros(shape)
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
 - Basically an image consists of pixels each having different values of Red,blue and green .My task requires to scan all the    RGB composition values , store and then apply modifications on it to make it suitable  to perform kmeans++ algorithm on it.

- After getting label and centroid lists, make a new list in which values of RGB are inserted as per algorithm.

- Finally create a new image from the new list of pixels.

## Solution

```python
from PIL import Image
from matplotlib import *
import numpy as np
from scipy.cluster.vq import kmeans2
inputpath=input("Enter the input path: ")
im=Image.open(inputpath,'r')

pix_val=list(im.getdata())
#print(im.size)

k=int(input("Enter the value of k: "))

pix_val_flat=[x for sets in pix_val for x in sets]

new_list1=[float(i) for i in pix_val_flat]
#print(new_list1)
new_list2=[]
b=len(new_list1)
i=0
while(b/3>0):
    small_list=[]
    a=1
    while(1>0):
        small_list.append(new_list1[i])
        i=i+1
        if(a%3==0):
            break
        a=a+1
    new_list2.append(small_list)
    b=b-3

z=new_list2
centroid, label = kmeans2(z, k, minit='++')

arr=np.array(centroid)
arr=arr.astype('uint8')
centroid=arr

print(centroid)

m=0
final_list=[]
while(m<len(label)):
    final_list.append(centroid[label[m]])

    m=m+1

x=0
'''
while(x<len(final_list)):
    y=0
    while(y<3):
        z[x][y]=final_list[x][y]
        y=y+1
    x=x+1
print(final_lis3t[1])'''
new=[]
while(x<len(final_list)):
    new.append(tuple(final_list[x]))


    x=x+1
'''
print(new)
im2= Image.new(im.mode,im.size)
im2.putdata(new)'''



print(new)
im2=Image.new(im.mode,im.size)
im2.putdata(new)
im2.show()
outputpath=input("Enter the output path: ")
im2.save(outputpath)
```


# 4. Riya Agrawal
 
 ## Problem
- Gaussian noise is statistical noise having probability distribution function equal to that of normal distribution, also     known as gaussian distribution. In simple words, the values that noise can take on are gaussian distributed. 
- My task was to first generate a sin wave and than add gaussian noise to it with mean zero and particular variance and Then   we filter that wave to reduce noise.
- Functions are defined using numpy and then we plot a sine wave with specific parameters.
- Finally the plots depicts the difference.

## Solution

```python
import numpy as np
import math
import matplotlib.pyplot as plt

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
  
clean_sin = generate_sin_wave(2, (-2,8), 1000)
plt.plot(clean_sin)
f,ax = plt.subplots()
ax.plot(clean_sin)
plt.savefig("clean_sin")
plt.show() 

dirty_sin = noisify(clean_sin, 0.05**2)
plt.plot(dirty_sin)
f,ax = plt.subplots()
ax.plot(dirty_sin)
plt.savefig("dirty_sin")
plt.show()

cleaned_sin = mean_filter(dirty_sin, 1)
plt.plot(cleaned_sin)
f, ax = plt.subplots()
ax.plot(cleaned_sin)
plt.savefig("cleaned_sin")
plt.show()  



```

---

<img src = "meme.jpeg" width = 350 align = "center">
