import argparse
import os
import scipy
from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
import utils
print("scipy version: ", scipy.__version__)

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str)
parser.add_argument('--k', type=int)
parser.add_argument('--output', type=str)

args = parser.parse_args()

k = args.k
assert k < 51 and k > 0
assert os.path.isfile(args.input), 'input({}) is not a valid file'.format(args.input)

def transform_img(arr, k):
    original_shape = arr.shape
    assert arr.ndim == 3 and arr.shape[2] == 3, 'invalid arr. shape = {}'.format(arr.shape)
    arr = arr.astype('float').reshape((-1, 3))
    centroid, label = kmeans2(arr, k=k, iter=10,minit='++', check_finite=False)
    kimg = centroid[label].reshape(original_shape)
    return utils.clip_both_sides(kimg)

img = utils.load_image(args.input, rescale=False, grayscale=False)
tri = transform_img(img, k = args.k)
utils.make_fig(tri, cmap=None)
plt.savefig(args.output, cmap=None)
