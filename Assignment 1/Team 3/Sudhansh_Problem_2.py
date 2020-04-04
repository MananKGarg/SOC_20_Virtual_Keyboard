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
