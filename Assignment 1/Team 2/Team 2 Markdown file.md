
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
    > Solution can be described as follows:-
        > * First we take data input and separate different data from input using
        split command and store it separately
        >  * Then we create a dictionary of players and their respective score for first
        match
        > * We iterate the loop the number of matches we have to store
        >  * Then we create another dictionary which contain match name as key
        and the value as dictionary made in step number 2.
        >  * Next we make a separate list of all the players that take part , taking care
        we do not repeat their name
        >  * Now we make a loop and iterate it over each player name , to take care
        of the multiple entries of a player
        >  * Next we make a tuple of player_name and total run score and add it into
        a list
        >  * Finally we sort the list in decreasing order of run scored and
        lexicographically if score is same.

* ## Solution

``` python
def f(list,element):
    for i in list:
        if i==element: return True
    else: return False
save_match=[]
save_score=[]
match_score = dict()
n=input()
for y in range(0,int(n)):
    score = dict()
    data = input('Enter match & scores separated by ":" ')
    temp = data.split(':')
    match_name = temp[0]
    save_match.append(match_name)
    player_run = temp[1].split(',')
    count=len(player_run)
    for x in range(0,count):
        actual = player_run[x].split('-')
        score[actual[0]] = int(actual[1])
    save_score.append(score)
    match_score[save_match[y]] = save_score[y]
print(match_score)
i=0
list=[]
for i in range(0,int(n)):
    for p, q in save_score[i].items():
        if f(list,p) == False:
            list.append(p)

final=[]
for pl in list:
    total=0
    for i in range(0,int(n)):
        for p, q in save_score[i].items():
            if pl==p:
                total=total+q
    final.append((pl,total))

print(sorted(final,key=lambda x:(-x[1],x[0])))

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
# 3. Paarth Jain

* ## Problem
  > We have to use the Kmeans++ algorithm to divide the given coloured image into k (given in the question) clusters(based on the pixelvalue).
  Each cluster has a centroid. The pixelvalue of each pixel belonging to a certain cluster is changed to the central pixelvalue.
  This way we construct a new array and hence a new image.

* ## Solution
```python
import numpy as np
import imageio
from scipy.cluster.vq import kmeans2

path = input()
k = int(input())

data_original = imageio.imread(path)
h,w,a = np.shape(data_original)     #a always has a value 3. it is written here just to avoid error 

data_2d = np.ones((h*w,3))
for i in range(h):
    data_2d[i*w:(i+1)*w,:] = data_original[i,:,:]
 
clusters,labels = kmeans2(data_2d,k, minit = '++')

data_new_2d = np.zeros((h*w,3))
for i in range(h*w):
    data_new_2d[i] = clusters[labels[i]]

data_new = np.zeros((h,w,3))
for i in range(h):
    data_new[i,:,:] = data_new_2d[i*w:(i+1)*w,:]

data_new  = data_new.astype('uint8')        #to avoid 'lossy conversion' warning
imageio.imwrite(path,data_new)

```

# 4. Tanisha Khandelwal

* ## Problem
  >in this problem we need to create three functions-
mean_filter-creates a floating array of a 1d array given kernel size
generate_sine_wave- generates an array having samples of sine wave
noisify-adds gaussian noise with zero mean and variance to array
 
using created functions we create another function driver with given conditions

* ## Solution
```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.stride_tricks import as_strided


def mean_filter(arr, k):  # creating mean-filter function
    n = len(arr)
    list = np.empty([n + 2 * k])
    list[k:n + k] = arr[0:]
    list[0:k] = arr[::-1][-k:]
    list[n + k:n + 2 * k] = arr[::-1][:k]
    stride = list.strides[0]
    new = as_strided(list, shape=(n, 2 * k + 1), strides=(stride, stride))
    output = np.sum(new, axis=1)
    return output / (2 * k + 1)


def generate_sine_wave(period, range_, num):  # creating sine wave function
    x = np.linspace(range_[0], range_[1], num)
    y = np.sin(2 * x * np.pi / period)
    return y


def noisify(array, var):  # adding gaussian noise with 0 mean and given variance
    output = array + np.random.normal(0, np.sqrt(var), len(array))
    return output

    def driver():
        a = np.arange(-2, 8, 1000)
    clean_sin = generate_sine_wave(2, [-2, 8], 1000)
    dirty_sin = noisify(clean_sin, 0.0025)
    cleaned_sin = mean_filter(dirty_sin, 1)
    plt.plot(a, clean_sin)
    plt.savefig("clean_sin.png")
    plt.plot(a, dirty_sin)
    plt.savefig("dirty_sin.png")
    plt.plot(a, cleaned_sin)
    plt.savefig("cleaned_sin.png")


    driver()

```

## MEME
## *Breaking Fast*

![Breaking Bad Meme](https://pics.me.me/im-not-always-in-scenes-of-breaking-bad-but-when-53538255.png "Mom Where's My Breakfast")
