import sys
from PIL import Image
import numpy as np

def convolve(T,im):
    arr = np.array(im)
    t = np.array(T)
    l = arr.shape[0] - t.shape[0] + 1
    b = arr.shape[1] - t.shape[1] + 1
    new_arr = np.zeros(arr.shape)

    for i in range(l):
        for j in range(b):
            new_arr[i][j] = np.sum(t*arr[i:i+t.shape[0],j:j+t.shape[1]])
    return new_arr

im = Image.open(sys.argv[1])
im = im.convert('L')
T = [[1,1,1,1,1],[1,-3,3,-3,1],[1,-3,8,-3,1],[1,-3,3,-3,1],[1,1,1,1,1]]
new = convolve(T,im)
new = Image.fromarray(255*new/np.max(new))
print('Convolution:\n',np.array(T))
im.show()
print('original:',im.size)
new.show()
print('convolved:',new.size)