matches = {}                                            #first output
total_scores = []                                       #second output
plscr = {}                                              #stores player scores temporarily.
for _ in range(int(input())):
    match_name = input().split(':',)                    #match_name[0] is the match's name.
    matches[match_name[0]] = {}
    temp1 = match_name[1].split(',')                  #stores '-' seperated player name,score temporarily.
    for j in range(len(temp1)):
        temp2 = temp1[j].split('-')                     #temp2[0] is player name and [1] is score.
        matches[match_name[0]][temp2[0]] = temp2[1]     #store score in nested dictionary.
        if temp2[0] in plscr:                           #add to previous score or create new player.
            plscr[temp2[0]] += int(temp2[1])
        else:
            plscr[temp2[0]] = int(temp2[1])    

for pl, sc in plscr.items():                            #form a list of tuples of keys and indexes.
    total_scores.append((pl,sc))   
        
print(matches)
print(total_scores)
