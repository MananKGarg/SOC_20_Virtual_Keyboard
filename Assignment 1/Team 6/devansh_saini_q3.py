from PIL import Image
from matplotlib import *
import numpy as np
from scipy.cluster.vq import kmeans2
inputpath=input("Enter the input path: ")
im=Image.open(inputpath,'r')

pix_val=list(im.getdata())
#print(im.size)

k=int(input("Enter the value of k: "))

pix_val_flat=[x for sets in pix_val for x in sets]

new_list1=[float(i) for i in pix_val_flat]
#print(new_list1)
new_list2=[]
b=len(new_list1)
i=0
while(b/3>0):
    small_list=[]
    a=1
    while(1>0):
        small_list.append(new_list1[i])
        i=i+1
        if(a%3==0):
            break
        a=a+1
    new_list2.append(small_list)
    b=b-3

z=new_list2
centroid, label = kmeans2(z, k, minit='++')

arr=np.array(centroid)
arr=arr.astype('uint8')
centroid=arr

print(centroid)

m=0
final_list=[]
while(m<len(label)):
    final_list.append(centroid[label[m]])

    m=m+1

x=0
'''
while(x<len(final_list)):
    y=0
    while(y<3):
        z[x][y]=final_list[x][y]
        y=y+1

    x=x+1

print(final_lis3t[1])'''
new=[]
while(x<len(final_list)):
    new.append(tuple(final_list[x]))


    x=x+1
'''
print(new)

im2= Image.new(im.mode,im.size)
im2.putdata(new)'''



print(new)
im2=Image.new(im.mode,im.size)
im2.putdata(new)
im2.show()
outputpath=input("Enter the output path: ")
im2.save(outputpath)
