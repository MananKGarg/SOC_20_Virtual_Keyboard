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
	black_count = np.zeros(shape)
	white_count = np.zeros(shape)
	mid_count = np.zeros(shape)
	mid_total = np.zeros(shape)
	picture = np.zeros(shape)

	for (r1,c1,r2,c2),value in input_dict.items():
		value = np.array(value)
		white_count[r1:r2,c1:c2] += np.where(value == 255,1,0)
		black_count[r1:r2,c1:c2] += np.where(value == 0,1,0)
		mid_count[r1:r2,c1:c2] += np.where(np.logical_and(value>0,value<255),1,0)
		mid_total[r1:r2,c1:c2] += np.where(np.logical_and(value>0,value<255),value,0)

	picture[np.logical_and(black_count<=white_count,white_count!=0)] = 255 
	clean = np.where(mid_count!=0)
	picture[clean]=mid_total[clean]//mid_count[clean]	
	
	return picture
