# <cool_team_name>

>Talk less, Code more...

|Problem Number |Team member |
|--- |--- |
|Problem 1 |[Aashuraj Hassani](https://github.com/aashurajhassani "Go to the GitHub profile.") |
|Problem 2 |[Sudhansh](https://github.com/Sudhansh6) |
|Problem 3 | [Pavithra]( https://github.com/PavithraB10) |
|Problem 4 |[Vishesh Agarwal](https://github.com/Vishesh2k01) |

## 1. Aashuraj Hassani

- Problem

>The problem is basically on the use of lists and dictionaries. We input the stats of each match in a proper format and then contruct and print the dictionary containing all stats in a structured manner, followed by a list containing tuples (name, total-score).

- Solution

```python
# getting the number of matches
while True:
       try:
              num_matches = int(input('Enter the number of matches- '))
              break
       except ValueError:
              print('Invalid input. Please enter a valid input i.e. an integer')
# the number of matches played is stored in variable num_matches

print("To input the stats, use format-\n<match_name>:<player_name>-<runs>,<player_name>,<run>,...")

main_dict={} # this is the main dictionary which is needed as output

for i in range(num_matches):
       stats = str(input())
       stats = stats.replace(':',' ')
       stats = stats.replace('-',' ')
       stats = stats.replace(',',' ')
       stats_list = stats.split()

       match_name = stats_list[0]

       stats_list.remove(match_name)

       player_name_list = []
       for words in stats_list:
              if (stats_list.index(words)%2==0):
                     player_name_list.append(words)

       player_runs_list = []
       for words in stats_list:
              if (stats_list.index(words)%2==1):
                     player_runs_list.append(int(words))

       nest_dict = dict(zip(player_name_list,player_runs_list))

       main_dict[match_name] = nest_dict

print(main_dict)

import pandas as pd
import numpy as np
table = pd.DataFrame(main_dict)
table.fillna(0, inplace=True)
table['total_runs'] = table.apply(np.sum,axis=1)

total_runs_list = list(table['total_runs'])
for i in range(len(total_runs_list)):
       total_runs_list[i]=int(total_runs_list[i])
players_list =  table.index.values.tolist()

player_total = []
for i in range((len(players_list))):
       tup = (players_list[i],total_runs_list[i])
       player_total.append(tup)

player_total.sort(key=lambda pair:pair[0], reverse=True) # first sorting in decreasing lexicographic order of player name as this is the second priority
player_total.sort(key=lambda pair:pair[1], reverse=True) # now finally sorting in decreasing order of total runs as this is the first priority
print(player_total)
```
## 2. Sudhansh

- Problem 

> The problem tests our understanding of the python and numpy library. An array consisting of patches(having intensity at each pixel) of a picture is taken as input. The data is analysed and the picture is put together using the algorithm. The numpy library is used to work out the calculations and the final array having the intensities in the picture is returned.

- Solution
 
```python
import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
	"""
	input_dict:
	key: 4-tuple: (topleft_row, topleft_col, bottomright_row,
	bottomright_col): location of the patch in the original image.
	topleft_row, topleft_col are inclusive but bottomright_row,
	bottomright_col are exclusive. i.e. if M is the reconstructed matrix.
	M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the
	patch.,
	value: 2d np array: the image patch.
	shape: shape of the original matrix.
	"""
	black_count = np.zeros(shape)
	white_count = np.zeros(shape)
	mid_count = np.zeros(shape)
	mid_total = np.zeros(shape)
	picture = np.zeros(shape)

	for (r1,c1,r2,c2),value in input_dict.items():
		value = np.array(value)
		white_count[r1:r2,c1:c2] += np.where(value == 255,1,0)
		black_count[r1:r2,c1:c2] += np.where(value == 0,1,0)
		mid_count[r1:r2,c1:c2] += np.where(np.logical_and(value>0,value<255),1,0)
		mid_total[r1:r2,c1:c2] += np.where(np.logical_and(value>0,value<255),value,0)

	picture[np.logical_and(black_count<=white_count,white_count!=0)] = 255 
	clean = np.where(mid_count!=0)
	picture[clean]=mid_total[clean]//mid_count[clean]	
	
	return picture
```

## 3. Pavithra

- Problem

> The problem requires the use of SciPy(KMeans) and NumPy libraries. It also involves using loops and functions from pillow to edit the given image.

- Solution

```python
import os, sys
from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2

input_file = Image.open(sys.argv[2],mode='r')
k = int(sys.argv[4])
output_file = open(sys.argv[6],'r+') 

size = input_file.size
input = input_file.load()
data = []
for x in range(size[0]):
	for y in range(size[1]):
		data.append(tuple(input[x,y]))
    
data = np.array(data)
data = data.astype('float64')	

centroid, label = kmeans2(data,k,minit='++')

np_label = np.array(label)
for x in np.unique(np_label):
	data[np_label==x] = centroid[x]

picture = Image.new("RGB",size)
data = data.astype('int64')
pic = picture.load()
print(data)
for x in range(size[0]):
	for y in range(size[1]):
		pic[x,y] = tuple(data[x*size[1]+y]) 
```

## 4. Vishesh Agarwal

- Problem

> In this problem, three functions are to be created (mean_filter, generate_sign_wave, noisify) which will be used in driver.py.

- Solution

```python
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def mean_filter(a,k):
	
	l = len(a)
	b = np.zeros(l)
	k1 = a[k-1:0:-1]+[a[0]]		#[a[0]]*a[0]
	k2 = a[l:l-k-1:-1]		#[a[l-1]]*a[l-1]
	a_ = np.array(k1+a+k2)
	b = np.around(list(map(lambda i:np.average(a_[i-k:i+k+1]),range(k,k+l))),1)
	return b


# mean_filter([1,2,3,4,5,6,7,8,9],2)

def generate_sin_wave(period, range_,num):
	a=range_[0]
	b=range_[1]
	d=(b-a)/(num-1)
	i=1
	while (i<=num):
		p= a+ (i-1)*d
		q=math.sin(6.28*p/period)
		x.append(p)
		clean_sin.append(q)
		i=i+1

	return x,clean_sin


def noisify(array, var):
	return (array+np.random.normal(0,var,1000))


noise=noisify(clean_sin,var)
dirty_sin=clean_sin+noise
```

![meme](https://scontent.fhyd13-1.fna.fbcdn.net/v/t1.0-9/92665420_1049775758742141_7293480417141719040_n.jpg?_nc_cat=106&_nc_sid=825194&_nc_ohc=YfbjBa8NLqsAX9QnPhq&_nc_ht=scontent.fhyd13-1.fna&oh=9b6781d8e51a71aab75cab5f5971aa42&oe=5EAF7EEE)
