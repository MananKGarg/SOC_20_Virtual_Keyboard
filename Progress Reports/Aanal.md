## Progress Report for SoC: Virtual Keyboard.
#### Mentor - Manan K. Garg
#### Mentee - Aanal Sonara
#### Roll no. - 190070064
#### Branch - Electrical, 1st year UG
### About project: 
The project is relatively new in SoC conducted (instructed) by our mentor Manan K. Garg. This project is about using augmented reality to make our lives easier by space-efficient devices. Virtual keyboard is easily portable which makes it a very suitable substitute of keyboards. It's also very useful to write long texts on small screens. 


![](http://pixel.brit.co/wp-content/uploads/2014/06/DadGiftsVirtualKeyboard.jpg) 

### Task 1:
The first part of this task was to [dual boot](https://www.youtube.com/watch?v=u5QyjHIYwTQ) my laptop. The steps briefly are:
* Download Linux OS
* Partition your hard-drive
* Download etcher.io 
* Flash a pen drive using etcher
* Restart and press F10 or F12 to enter into live ubuntu environment
* Install Ubuntu.

The second part was learning about [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) which includes files with .md extension. 
* There are six types of headings
* We can add images as !(image name)[image link]
* We can add links as [link text](link address)
* We can use italics with * or _ and bold with ** or __ 
* Unordered Lists can be made as '*', '-' or '+'
* Ordered lists can be made as 1., 2., then ⋅⋅1. for ordered sub-list and ⋅⋅* for unordered sub-list
* We can also add tables.
* Codes are written as  '''python  (code) '''
* To add horizontal line ' _ ' (3 or more), it appears as follows
____
* We can also use raw HTML in your Markdown, and it'll mostly work pretty well.

The third part was learning about Git-hub. It's very useful to share codes and information. It's a very interactive platform where we can share our codes, information and ask for help to debug our codes or other software problems. My Git-hub account is [Aanal2901](https://github.com/Aanal2901). The [basics](https://guides.github.com/activities/hello-world/) of Git-hub include:
* Creating repository
* Creating branches
* Merging branches into master branch
* To make changes
* To pull requests


### Task 2:
The first part was to learn about python. It started with simple tutorials about python then learn about some special modules such as numpy, matplotlib and mathematical functions. Using python (and numpy) we can easily implement mathemtical functions and equations this will be useful in future as well for other applications like ML.
The references are as follows:
[Python basics](https://www.learnpython.org/), [Python](https://docs.python.org/3/tutorial/), [Python advanced](https://scipy-lectures.org/). Python advanced contains documentations for modules [numpy](https://scipy-lectures.org/intro/numpy/index.html) which is used for arrays and direct built-in functions for arrays and mathematical functions (such as generating random numbers, arrays, trigonometry functions, algebraic equations) and [matplotlib](https://scipy-lectures.org/intro/matplotlib/index.html) which is mostly used for plots. We use it to plot data (scatter plot, histogram, bar plot, 3D plots) and it provides a lot of options to edit plots such as color, range, type of line, labelling. 

The second part was an assignment. Each team member was given one question. The questions covered four topics in particular:
1) This question was about handling dictionaries in python. This showed very efficient way of using dictionary and how it simplifies rather tedious work of using for loops which also require more execution time.
2) Salt and Pepper noise - This question was about patching the image by using average values of pixels, and make a function to store it's average values and use when area of different patches overlap.
3) This question uses a machine learning algorithm of K-means clustering. In this algorithm we make K clusters and use their centroid value for entire cluster.
4) This question required us to make three mathematical functions hence we make use of numpy.

### Task 3:
The first part was to learn about opencv module.  It means Open Computer Vision, which contains a lot of libraries and in-built funtions which help us with image processing. I followed [video tutorials](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) and [GeeksforGeeks tutorials](https://www.geeksforgeeks.org/opencv-python-tutorial/) to learn opencv. It has different functions such as:
* Resizing, rescaling, rotating and edge detection image
* Thresholding  (it's different types) image (useful to remove noises)
* Filtering a color (color segmentation) in image
* Denoising colored images 
* Background substraction
* Foreground extraction
* Video capture
* face detection using webcam and opencv
* morphological operations (used to extract image components also smoothen images and remove noise)


The second part was to make 2 files each for different functions of opencv in github opencv-master [folder](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/tree/master/SoC_OpenCV-master). I wrote about Canny-edge detection [(here)](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/20.%20%20(Aanal)%20Canny%20Edge%20Detection%20in%20OpenCV.md) and detect corners with harris corner detection method [(here)](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/37.%20%20(Aanal)%20Detect%20Corners%20with%20Harris%20Corner%20Detector.md). Canny edge is used to detect all/most edges in a picture using five step algorithm. Corner detection is done by the fact that intensity gradient of a pixel drastically changes in all directions. 


The third part was to write a code for [invisibility cloak](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Invisibility%20Cloak/Aanal.md). The algorithm followed was:
* Store the background in the first frame.
* Now the video starts, so appear in front of web-cam and use red color cloth as cloak. 
* The red color will be segmented using color segmentation (red-mask)
* Red color has two ranges in HSV so we make two masks and add them
* From the frame, this red part is removed
* Using red mask we extract back-ground part which appears instead of red cloth
* Using inverse of mask (to get non-red part which will be foreground) we get the frame without red part
* Adding the above two images, we get final image with fore-ground and back ground in place of red-cloth.
* To use any other color for cloak, change mask range.

### Task 3:
The final task was to make a paper keyboard. To do this we first need a paper keyboard (with a proper outline to get proper contour), then use the webcam to use it as a keyboard. The code is provided [here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/tree/master/Paper%20Keyboard). To complete this task we first had to learn how to make a sudoku solver and some of it's concepts such as perspective transformation were integrated in this project too. The algorithm followed is:
* First use thresholding, perspective transformation on the image to get only the keyboard.
* Decide which space would be considered which key. I used a dictionary to make it wasy.
* Now for each frame of the video, find the difference between this frame and keyboard
* Find the top most point of the contour of this difference image.
* Check where this point lies in the keyboard.
* Check if it is pressed for more than a second, in that case consider it pressed.
Please note a few things:
* I could not arrange for a paper keyboard, hence my code may face a few bugs, I tried to reduce as many as I could.
* I can only use one finger at a time.
* Since I have to wait for a second to press a key it is slower than conventional keyboard. 

#### Despite being slower than the conventional keyboard it is still a step forward towards conputer vision and augmented reality. And surely in the future we will develop better methods/algorithms for virtual keyboard and other devices to solve the problems of space occupancy, transport/ portability etc. And I am grateful I got to be a part of this project. I may not have perfectly completed it, but it was a wonderful learning experience. 
