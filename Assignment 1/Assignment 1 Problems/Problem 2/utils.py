import numpy as np
import pickle
from PIL import Image
from matplotlib import pyplot as plt

def noisify(inp, noise_type, val):
    imshape = inp.shape
    if (noise_type == 'gauss'):
        # val is sigma
        noise = np.random.normal(0, val, imshape)
        return inp + noise

    if (noise_type == 'salt_and_pepper' or noise_type == 'sap' or noise_type == 's&p'):
        # val is fraction of corrupted pixels
        p_by_2 = val / 2.0
        randmat = np.random.random(imshape)
        zero_mask_inv = np.logical_not(randmat < p_by_2)
        one_mask = randmat > (1 - p_by_2)
        out_img = np.multiply(inp, zero_mask_inv)
        return clip_both_sides(np.maximum(out_img, one_mask*255))

def rescale_mat(npa):
    minn, maxx = np.amin(npa), np.amax(npa)
    if (minn != maxx):
        npa = (npa - minn) / (maxx - minn)
        return npa
    elif (minn >= 0 and maxx <= 1):
        return npa
    elif (minn >= 0 and maxx <= 255):
        return (npa / 255.0)
    else:
        print("unable_to_rescale")
        return np.zeros(npa.shape)

def rgb2gray(rgb): # copied from https://stackoverflow.com/a/12201744
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def clip_both_sides(arr):
    arr = np.rint(arr)
    arr[arr < 0] = 0
    arr[arr > 255] = 255
    arr = arr.astype('int')
    return arr

def load_image(infilename, rescale=False, grayscale=True):
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int")
    # print('data', data)
    if grayscale:
        data = rgb2gray(data)
    if rescale:
        data = rescale_mat(data.astype('float'))
    else:
        data = clip_both_sides(data)
    return data

def make_fig(nparr, cmap='gray', title=None):
    plt.figure()
    if type(title) == str:
        plt.title(title)
    if (cmap is None):
        plt.imshow(nparr)
    else:
        plt.imshow(nparr, cmap=cmap)

def load(filename):
    with open(filename, 'rb') as f:
        loaded = pickle.load(f)
    return loaded

def save(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, protocol=4)
    return
