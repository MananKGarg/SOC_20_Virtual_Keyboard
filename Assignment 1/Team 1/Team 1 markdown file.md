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
list_players=[]
listt=[]
for key,value in dict1.items():
    for keys in value:
        list_players.append((keys))
        listt.append((value[keys]))

final_list =[]
for i in range(len(list_players)):
    if list_players.count(list_players[i])>1:
        for j in range(i+1, len(list_players)):
            if list_players[j]==list_players[i]:
                listt[i] += listt[j]
                listt[j]=0
                list_players[j]=0
t=list_players.count(0)
for i in range(t):
    list_players.remove(0)
    listt.remove(0)

for i in range(len(listt)):
    final_list.append((list_players[i],listt[i]))

final_list = sorted(final_list, key = lambda x: x[1], reverse=True)
print(final_list)

```
