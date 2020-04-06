# Team - 4 (Runtime Terror)
>while(noSuccess) {
        tryAgain();
}

|__Problem Number__|__Team Member__|
|------------------|---------------|
|Problem 1|[Nirmal Shah](https://github.com/nirmalshah123)|
|Problem 2|[Sharvaree Sinkar](https://github.com/sharvaree1921)|
|Problem 3|[Harsh Kumar](https://github.com/gautam32)|
|Problem 4|[Aayush Shrivastava](https://github.com/aayush2200)|

## 2. Sharvaree Sinkar
* __Problem__
    >The main task of this problem is to reduce the salt and pepper noise in the gray scale image.
    Here, we are sequentially scanning each mentioned patches for the no. of pixels at each location
    of image. For that we are given an input dictionary with keys as 'tuples' and keywords as 'array 
    of pixels'. We have to keep record of black_count, white_count, mid_count, mid_total at each pixel of 
    image and change it according to the given algorithm. If mid_count is non-zero, change mid_total to 
    mid_total//mid_count. If black_count > white_count then put '0' and if black-count <= white_count then
    put 255. Where no patches fall put '0' there. Likewise we have to reconstruct the matrix M of pixels.
    
* __Solution__
```python
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
 ```

## 4. Aayush Shrivastava
* __Problem__
    >The problem asked for generating samples of a pure sine wave
    and adding gaussian noise to it then clearing that noise using
    mean filter. The problem asked for defining three main functions
    first which applies mean filter to an input array, second a function
    to generate an array which stored samples of a sine wave whose period
    and range is given through parameters and lastly a gaussian noise
    adding function. A driver function was also written which generated
    a clean sine wave, plotted it and saved the plot then it added gaussian
    noise to clean sine, plotted it and saved it and then cleaned that
    sine using mean filter, plotted it and saved it.

* __Solution__
```python
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10 ** 5)                          # mean_filter was having too many recursions
                                                        # to increase recursion limit

i = 0


def mean_filter(arr, k):
    global i
    if (len(arr) - i) >= (2 * k + 1):                   # applying mean filter to the input array
        sub_arr = arr[i:i + (2 * k + 1)]
        mean = np.mean(sub_arr)
        arr[i + k] = mean
        i = i + 1
        mean_filter(arr, k)

    i = 0
    return arr


def generate_sin_wave(period, num, *range_):
    x = np.linspace(range_[0], range_[1], num)          # generates an array having samples of sine wave
    y = np.sin(2 * x * np.pi / period)
    return y


def noisify(array, var):
    noise = np.random.normal(scale=np.sqrt(var), size=len(array))
    noise_array = noise + array                         # adds gaussian noise to the array passed
    return noise_array


def set_axes():
    ax = plt.gca()  #
    ax.spines['right'].set_color('none')                #
    ax.spines['top'].set_color('none')                  #
    ax.xaxis.set_ticks_position('bottom')               # for setting the axes at origin
    ax.spines['bottom'].set_position(('data', 0))       #
    ax.yaxis.set_ticks_position('left')                 #
    ax.spines['left'].set_position(('data', 0))         #

    plt.xlim(X.min() * 1.1, X.max() * 1.1)
    plt.xticks(np.linspace(-2, 8, 11))                  # Setting x ticks
    plt.yticks(np.linspace(-1, 1, 5))                   # Setting y ticks


X = np.linspace(-2, 8, 1000)


def driver_function():
    clean_sin = generate_sin_wave(2, 1000, -2, 8)
    set_axes()
    plt.plot(X, clean_sin, label='clean_sin')           # plotting clean sin
    plt.legend(loc='upper right')
    plt.savefig('clean_sin.png')                        # saving the file
    plt.close()

    plt.xticks(np.linspace(-2, 8, 11))
    dirty_sin = noisify(clean_sin, 0.05 * 0.05)
    set_axes()
    plt.plot(X, dirty_sin, label='dirty_sin')           # plotting dirty sin
    plt.legend(loc='upper right')
    plt.savefig('dirty_sin.png')                        # saving the file
    plt.close()

    cleaned_sin = mean_filter(dirty_sin, 1)
    set_axes()
    plt.plot(X, cleaned_sin, label='cleaned_sin')       # plotting cleaned sin
    plt.legend(loc='upper right')
    plt.savefig('cleaned_sin.png')                      # saving the file
    plt.close()


driver_function()
```

![](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/Team-4/Assignment%201/Team%204/meme.png)
