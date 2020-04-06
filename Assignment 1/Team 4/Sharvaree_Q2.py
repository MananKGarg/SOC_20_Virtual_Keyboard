import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):

    black_count = np.zeros(shape)        #
    white_count = np.zeros(shape)        #
    mid_count = np.zeros(shape)          #     Initialization of black_count,white_count,mid_count,mid_count,mid_total,M
    mid_total = np.zeros(shape)          #
    M = np.zeros(shape)                  #

    for (topleft_row, topleft_col, bottomright_row, bottomright_col),y in input_dict.items():  # no loop except this!
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)]
        x = np.array(patch)

        b_c = black_count[tlr:brr, tlc:brc]
        w_c = white_count[tlr:brr, tlc:brc]        # declaring subarrays according to patch
        m_c = mid_count[tlr:brr, tlc:brc]
        m_t = mid_total[tlr:brr, tlc:brc]

        s = (x == 0)                               #
        t = (x == 255)                             #imposing conditions
        u = ((x > 0) & (x < 255))                  #

        b_c[s] = b_c[s] + 1                        #
        w_c[t] = w_c[t] + 1                        # updating each matrix sequentially according to patch
        m_c[u] = m_c[u] + 1                        #
        m_t[u] = x[u]  + m_t[u]                    #

    difference=black_count-white_count
    v = ((difference > 0) & (mid_count == 0))
    v1=np.any(v)
    r = ((difference < 0) & (mid_count == 0))
    r1=np.any(r)
    q=((mid_count!=0) )
    q1=np.any(q)
    a=(difference==0)
    a1=np.any(a)
    b=((black_count+white_count)==0)
    b1=np.any(b)

    if(a1==True):
        M[a]=255
    if(b1==True):
        M[b]=0
    if(q1==True):
        M[q]=mid_total[q]//mid_count[q]                   #Updating reconstructed matrix M.
    if(v1==True):
        M[v]=0
    if(r1==True):
        M[r]=255



    return M