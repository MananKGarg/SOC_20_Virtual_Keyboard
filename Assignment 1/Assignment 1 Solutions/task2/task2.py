import numpy as np
def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict: 
    key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are exclusive. i.e. if M is the reconstructed matrix. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.

    value: 2d numpy array: the image patch.

    shape: shape of the original matrix.
    """

    # Initialization
    M = np.zeros(shape, dtype='float')
    black_count, mid_count, white_count, mid_total = [np.zeros(shape, dtype='int') for _ in range(4)]

    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict:
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)]

        black_bool = patch == 0
        white_bool = patch == 255
        mid_bool = np.logical_not(np.logical_or(black_bool, white_bool))

        black_count[tlr:brr, tlc:brc][black_bool] += 1
        white_count[tlr:brr, tlc:brc][white_bool] += 1
        mid_count[tlr:brr, tlc:brc][mid_bool] += 1
        mid_total[tlr:brr, tlc:brc] += (patch * mid_bool).astype('int')

    midcntnz = mid_count > 0 # nz means non zero
    midcntz = np.logical_not(midcntnz) # z means zero
    mid_count[midcntz] = 1 # to prevent division by 0 error
    M += (mid_total / mid_count) * midcntnz
    M += (np.logical_and(black_count <= white_count, white_count > 0)) * midcntz * 255

    # could have used utils.clip_both_sides
    M = np.rint(M).astype('int')
    M[M<0] = 0
    M[M>255] = 255
    return M

