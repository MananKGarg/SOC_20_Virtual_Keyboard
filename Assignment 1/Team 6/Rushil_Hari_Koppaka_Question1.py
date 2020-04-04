match_name_list=[]                                          #initialising lists
match_list=[]
final_player_names=[]
final_scores=[]
while True :                                                 #getting main dictionary(entire league)
    match_name=input('enter match name,else: to finish type no \n')
    if match_name=='no':
        break
    else:
        match_name_list.append(match_name)
        single_match_dict = {}
        while True:                                           #getting inside dictionary(individua match)
            check=input('to go next match type no else press enter\n')
            if check=='no':
                break
            else:
                player_name,runs_scored=input('player name\n'),int(input('runs scored\n'))
                single_match_dict[player_name]=runs_scored
                if player_name in final_player_names:                                             #for tuple scorecard incrementing score of individual
                    final_scores[final_player_names.index(player_name)]+=runs_scored
                else:
                    final_player_names.append(player_name)
                    final_scores.append(runs_scored)

        match_list.append(single_match_dict)

final_dict=dict(zip(match_name_list,match_list))
print(final_dict)

scorecard=list(zip(final_player_names,final_scores))                #creating tuple list

s=sorted(scorecard,reverse=True)                                    #sorting names in decreasing lexicographic order
s2=sorted(s,key= lambda x:x[1],reverse=True)                        #sorting according to runs scored

print(s2)
