import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
	white_count = np.zeros(shape)
	black_count = np.zeros(shape)
	mid_total = np.zeros(shape)
	mid_count = np.zeros(shape)
	for (r1, c1, r2, c2), x in input_dict.items():
		white_count[r1:r2, c1:c2] += np.where(x == 255, 1, 0)
		black_count[r1:r2, c1:c2] += np.where(x == 0, 1, 0)
		x = np.mod(x, 255)
		mid_count[r1:r2, c1:c2] += np.where(x == 0, 0, 1)
		mid_total[r1:r2, c1:c2] += x

	mid_count = np.where(mid_count == 0, 1, mid_count)
	mid_total = np.divide(mid_total, mid_count)
	M = np.where(mid_total == 0, 255*(white_count >= black_count), mid_total)
	a = mid_total+white_count+black_count
	M = np.where(a == 0, a, M)
	return M

