# Team Name
## Tagline

| Problem Number    | Team Member |
| ----------------- | ----------- |
| Problem 1         |             |
| Problem 2         |             |
| Problem 3         |             |
| Problem 4         |             |


# 1. Aanal Sonara

## Problem Description:

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
