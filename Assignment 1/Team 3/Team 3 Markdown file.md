# Team 3 - Team_name

>Tagline

|Problem Number |Team member |
|--- |--- |
|Problem 1 |[Aashuraj Hassani](https://github.com/aashurajhassani "Go to the GitHub profile.") |
|Problem 2 |[Sudhansh](https://github.com/Sudhansh6) |
## 1. Aashuraj Hassani

- Problem

>The problem is basically on the use of lists and dictionaries. We input the stats of each match in a proper format and then contruct and print the dictionary containing all stats in a structured manner, followed by a list containing tuples (name, total-score).

- Solution

```python
# getting the number of matches
while True:
       try:
              num_matches = int(input('Enter tne number of matches- '))
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
> 
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
	black_count = np.zeros(shape)#,np.int64)
	white_count = np.zeros(shape)#,np.int64)
	mid_count = np.zeros(shape)#,np.int32)
	mid_total = np.zeros(shape)
	picture=np.zeros(shape)# ,np.int32)
	for key,value in input_dict.items():
		for i in range(0,key[2]-key[0]):
			for j in range(0,key[3]-key[1]):
				if(value[i][j]==0):
					black_count[key[0]+i][key[1]+j]+=1
				elif(value[i][j]==255):
					white_count[key[0]+i][key[1]+j]+=1 
				else:
					mid_count[key[0]+i][key[1]+j]+=1
					mid_total[key[0]+i][key[1]+j]+=value[i][j]
	# print(mid_count,'\n',black_count,'\n',white_count,'\n',mid_total)	
	picture[np.logical_and(black_count<white_count,mid_count==0)] = 255
	picture[np.logical_and(black_count==white_count,white_count!=0)] = 255 
	clean = np.where(mid_count!=0)
	picture[clean]=mid_total[clean]//mid_count[clean]

	return picture
```
