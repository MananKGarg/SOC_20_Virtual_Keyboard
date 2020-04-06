 n=int(input())   # Number of matches played

final_dict={}    
match_list=dict()

for j in range(n):
  data=input()
  mn=data.split(":")  #mn is match name + scores
  matchname=mn[1]     #sepearating mn into matchname and scores
  playerscore=matchname.split(",")

  for i in range(len(playerscore)):
    temp=playerscore[i].split("-")
    match_list[temp[0]]=int(temp[1])
    final_dict[mn[0]]=match_list

  match_list={}

print(final_dict)

#Now to add all the common entries

common_dict={}
for k, v in final_dict.items():
    for p in v:
        if p in common_dict:
            common_dict[p] += v[p]
        else:
            common_dict[p] = v[p]

print(common_dict)
print(sorted(common_dict.items(), key =lambda kv:kv[0],reverse=True)) #as we have to do lexicographic order only if scores match up

print(sorted(common_dict.items(), key =lambda kv:kv[1],reverse=True)) #This has to be done at the end as it is our main priority
