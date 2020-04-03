# Team 1 - Team_name

>Tagline

|Problem Number |Team member |
|--- |--- |
|Problem 1 |[Aashuraj Hassani](https://github.com/aashurajhassani "Go to the GitHub profile.") |

## 1. Aashuraj Hassani

- Problem

>The problem is basically on the use of lists and dictionaries. We input the stats of each match in a proper format and then contruct and print the dictionary containing all stats in a structured manner, followed by a list containing tuples (name, total-score).

- Solution

```
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
