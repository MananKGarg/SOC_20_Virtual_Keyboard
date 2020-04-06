import numpy as np

n=int(input())
dict1={}
final_dict={}
for i in range(n):
    data=input()
    sub_dict1={}
    data=data.split(":")
    data[1]=data[1].split(',')
    for j in range(len(data[1])):
        data[1][j]=data[1][j].split('-')
        sub_dict1[data[1][j][0]]=int(data[1][j][1])
        dict1[data[0]]=(sub_dict1)
        if data[1][j][0] in final_dict:
            final_dict[data[1][j][0]] += int(data[1][j][1])
        else:
            final_dict[data[1][j][0]] = int(data[1][j][1])
print(dict1)

data =[('name', 'U10'),('score', int)]
final_list = np.array(list(final_dict.items()), dtype=data)
final_list[::-1].sort(order= ['score', 'name'])

print(final_list)
