
## Team 2 - Heisenberg
> ***I AM THE DANGER***

|Problem Number |Team member |
|--- |--- |
|_Problem 1_ |[Kritin Agarwal](https://github.com/kritin7) |
|_Problem 2_|[Paarth Jain](https://github.com/Paarth-Jain)|
|_Problem 3_ |[Harshvardhan Ragade](https://github.com/WareWolf2002) |
|_Problem 4_ |[Tanisha Khandelwal](https://github.com/tanisha605) |

# 1. Kritin Agarwal

* ## Problem
    > Short Description

* ## Solution

``` python
#Code with highlighted syntax comes here

```

# 2. Paarth Jain
 
* ## Problem
  >In this problem we are given :-
  >
  > * overlapping noisy patches of an image.
  >     * It can be thought of as taking a clean image dividing it into patches and then adding salt and pepper noise to it. 
  > * The pixel data, and position of these patches are fed into the required function through a dictionary.
  > * We are also given the shape of the original image. 
  > 
  >Solving it involves the following steps :-
  > * For each pixel we maintain 
  >     * a black_count -> The number of times pixel value is 0.
  >     * a white_count -> The number of times pixel value is 255.
  >     * a mid_count -> The number of times pixel value was between between 0 and 255 (Both exclusive).
  >
  > * out of all patches that have a particular pixel in them, some(or all) would have acquired the s&p noise. Hence we can decide what pixel value should be accepeted during reconstruction using the following method :-
  >     * if mid_count is non zero mid_count/mid_total will be the correct value 
  >         * Ignoring 0 and 255 as they are the s&p noise.
  >         * Avg is being takaen because of some variations that might have occured during formation of patches etc.
  >     * if mid_count is zero :-
  >         * black_count> white_count ==> pixelvalue = 0
  >         * else ==> pixelvalue = 255
  > * Thus we have all the information we need to create the required image



* ## Solution
```python
import pandas as pd
import numpy as np
import imageio as im
test = pd.read_pickle('testcases.pkl')

def reconstruct_from_noisy_patches(input_dict, shape):
    M = np.zeros(shape)                         #Initializing arrays
    black_count = np.zeros(shape)
    white_count = np.zeros(shape)
    mid_count = np.zeros(shape) 
    mid_total = np.zeros(shape)

    for tlr, tlc, brr, brc in input_dict:
        patch = input_dict[(tlr,tlc,brr,brc)]

        white_count[tlr:brr,tlc:brc] += patch//255              #Changing counts using mathematical manipulation(because loops were not be used)(And loops would be really slow)
        black_count[tlr:brr,tlc:brc] += -1*((patch-1)//255)
        mid_total[tlr:brr,tlc:brc] += patch - 255*(patch//255)
        mid_count[tlr:brr,tlc:brc] += np.ones(patch.shape) - (patch//255 + -1*((input_dict[(tlr,tlc,brr,brc)]-1)//255))
    
    mid_0 = -1*((mid_count - 1)//mid_count.max())   
    mid_count += mid_0                              #replacing the positions with zero values with 1(so that mid_count/mid_total is defined)
    M = mid_total/mid_count                         #the positions with non zero mid_count values get their appropriate pixel value

    diff = white_count - black_count         #evaluating the difference matrix
    diff *= mid_0                           #filtering out the values where mid_count = 0

    value_0 = -1*(diff//(max(diff.max(),-1*diff.min())+1))          #filtering all the positions where black_count > white_count 
    value_225 = mid_0 - value_0
    M += 225*value_225                      #making the final changes 

    M = M.astype('uint8')               #to avoid 'lossy conversion' warning
    im.imsave('result.jpeg',M)          #saving the reconstructed and denoisified array into a .jpeg image file

reconstruct_from_noisy_patches(test[1][0],test[1][1])  #using appropriate indices to access the required arguments from the dictionary stored in testcases.pkl 






```
# 3. Harshvardhan Ragade

* ## Problem
  >Short Description

* ## Solution
```python
##Code with highlighted syntax comes here

```

# 4. Tanisha Khandelwal

* ## Problem
  >Short Description

* ## Solution
```python
##Code with highlighted syntax comes here

```

## MEME
## *Breaking Fast*

![Breaking Bad Meme](https://pics.me.me/im-not-always-in-scenes-of-breaking-bad-but-when-53538255.png "Mom Where's My Breakfast")
