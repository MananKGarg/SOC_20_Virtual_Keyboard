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
