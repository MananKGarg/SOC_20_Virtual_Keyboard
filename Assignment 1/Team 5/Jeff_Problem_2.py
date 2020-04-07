import numpy as np

def reconstruct_from_noisy_patches(input_dict, shape):
    N = len(input_dict)               #N is the number of patches
    black_count = np.zeros(shape)     #stores the black count in the corresponding cells                 
    white_count = np.zeros(shape)     #stores the white count in the corresponding cells 
    mid_count = np.zeros(shape)       #stores the mid count in the corresponding cells 
    mid_total = np.zeros(shape)       #stores the mid total in the corresponding cells
    image = np.zeros(shape)           #the final image matrix
    
    for patch in input_dict:
        tr = patch[0]                        #coordinates of top row
        lc = patch[1]                        #coordinates of left column
        br = patch[2]                        #coordinates of bottom row
        rc = patch[3]                        #coordinates of right column 
        
        white_count[tr:br,lc:rc] += input_dict[patch]//255                          #only cells with 255 become 1 
        black_count[tr:br,lc:rc] += (255 - input_dict[patch])//255                  #only cells with 0 become 1 
        mid_total[tr:br,lc:rc] += input_dict[patch] - (input_dict[patch]//255)*255  #non 255 cells added to mid total  
        mid_count[tr:br,lc:rc] += np.ones(input_dict[patch].shape)-(input_dict[patch]//255)-((255-input_dict[patch])//255)  
            
    image += np.nan_to_num(mid_total//mid_count)                  #image without white pixels
    
    black_white  = (white_count + black_count)//(white_count + black_count + mid_count) #cells that are black or white
    
    black_white  = np.nan_to_num(black_white)                    #fixing 0/0 divisions with nan_to_num            
    
    more_white = np.nan_to_num((2*white_count)//(white_count + black_count))  
    
    more_white = np.nan_to_num(more_white//more_white)            #cells with more white cells than black cells
    
    image += black_white * more_white * 255           #adding the white pixels
    
    image = image.astype(int)
    
    return image
