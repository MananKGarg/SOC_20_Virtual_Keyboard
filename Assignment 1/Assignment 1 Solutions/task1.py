n=int(input())
nested_dict={}
players_list=[]
for i in range(n):
    string=input()
    linei=[x for x in string.split(":")]
    nested_dict[linei[0]]={}
    players=[x for x in linei[1].split(",")]
    for x in players:
        sc=[y for y in x.split("-")]
        if(any(sc[0] in j for j in players_list)):
            indices = [i for i, tup1 in enumerate(players_list) if tup1[0] == sc[0]]
            update=players_list[indices[0]][1]+int(sc[1])
            del players_list[indices[0]]
            players_list.append((sc[0],update))
        else:
            players_list.append((sc[0],int(sc[1])))
        nested_dict[linei[0]][sc[0]]=int(sc[1])

print(nested_dict)
print(sorted(players_list,key = lambda item : (item[1],item[0]),reverse=True))

