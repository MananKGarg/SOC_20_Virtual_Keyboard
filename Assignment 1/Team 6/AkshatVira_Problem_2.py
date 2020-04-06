import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict:
    key: 4-tuple: (tlr, tlc, brr, brc):
            location of the patch in the original image. tlr, tlc are inclusive but brr, brc are exclusive.
            i.e. if M is the reconstructed matrix. M[tlr:brr, tlc:brc] will give the patch.
    value: 2d numpy array: the image patch.
    shape: shape of the original matrix.
    """

    black_count, white_count = np.zeros(shape), np.zeros(shape)
    mid_count, mid_total = np.zeros(shape), np.zeros(shape)
    M = np.zeros(shape)

    for tup, val in input_dict.items():
        tlr, tlc, brr, brc = tup
        white_count[tlr:brr, tlc:brc] += np.where(val == 255, 1, 0)
        black_count[tlr:brr, tlc:brc] += np.where(val == 0, 1, 0)
        mid_count[tlr:brr, tlc:brc] += np.where(np.logical_and(val != 0, val != 255), 1, 0)
        val = np.mod(val, 255)
        mid_total[tlr:brr, tlc:brc] += val

    #if mid_count != 0 final value is total/count
    #mid_total = np.where(mid_count == 0, mid_total, np.divide(mid_total, mid_count))
    mid_total = np.divide(mid_total, mid_count + (mid_count == 0))
    #if mid_count is 0 & white>black put 255 else put 0
    mid_total = np.where(mid_count == 0, np.where(white_count >= black_count, 255, 0), mid_total)

    #if no patch then put 0
    M = np.where(mid_count + white_count + black_count == 0, 0, mid_total)

    return M
