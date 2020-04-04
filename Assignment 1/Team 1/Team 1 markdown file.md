# Aanal_Assignment1_question1
## Problem Description:
##### The question is a collection of data of different cricket matches and then arranging it in dictionary fashion and as a list according to player and their scores.
##### Thus the problem requires us to know to about dictionaries and lists in python.
##### The data collected is in string format which has to be splitted first between matches, then players. 
##### After that it is stored in a dictionary which forms a nested dictionary with player name and corresponding score.
##### To print the list of players and their total score across all matches I first got an array of players and their score, and collected their total scoreand deleted the other occurences of same player in the array and converted it to a list.
##### Finally I printed the list by sorting it as per the second element of each sublist.
##### I am posting my code below:
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
