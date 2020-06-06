# **Week-1-progress**
Documentation of what I learnt in the week-23rd to 29th march 2020

# GitHub Account
## What is GitHub?
GitHub is an online platform where people can share their codes on a particular project and get reviewed from others.Here,one can also see the work done by others on various interesting projects.
## GitHub Essentials-->
GitHub essentials consist of -
1. Creating repositories(organization of a single project)
2. Creating branches(working on various parts/versions of the same repository)
3. Make and commit changes(if one wishes to change any particular part of code or some statements )
4. Pull request(propsing your changes to someone else to get reviewed)
5. Merge request(merging the branch reviewed by others into the master branch)

_This is how a particular project can be made organized and working on it becomes simpler and more collaberative_

References-[GitHub Basics](https://guides.github.com/activities/hello-world/)

# Dual Boot Ubuntu 18.04 and Windows 10
I dual booted my Windows 10 OS with Ubuntu 18.IN
04 OS.
Ubuntu is considered as most secured open source OS and is most popular linux OS.
Ubuntu has preinstalled python IDE(Integrating Development Environment)
However,installation of PyCharm makes it more convinient for programmers to save python files and to work on them.
Along with python,libraries such as Numpy,Scipy and Matplotlib helps in writing programs of multidimensional numerical arrays,scientific expressions and plotting figures respectively.

References-[Dual Boot setup](https://www.youtube.com/watch?v=u5QyjHIYwTQ)

# Markdown(Lightweight Markup Language)
Any files with .md extension are markdown files.Markdown language is extensively used to write files precisely.
Markdown Files are very easy to write and handle.It has its own cheatsheet to follow.Markdown is often used to format readme files,for writing messages in online forums,and to create rich text using a plain text editor.
References-[Markdown cheatsheet](https://www.youtube.com/watch?v=bpdvNwvEeSE)

# Python Basics-->
Python is a high level programming language which is easy to understand by its code.It is widely used by software developers,programmers,etc.
In this,we learnt the foolowing-->
## 1]Introduction to Python-
1. Numbers
2. Strings
3. List
## 2]Loops and functions-->
1. If statement
2. for statement
3. The range() function
4. break and continue statements
5. pass statements
6. Defining functions-
  6.1- Default Argument values
  6.2- Keyword Arguments
  6.3- Special Parameters
      6.3.1- positional-or-keyword arguments
      6.3.2- positional only arguments
      6.3.3- keywords only arguments
  6.4- Arbitrary argument lists
  6.5- Unpacking Rgument List
  6.6- Lambda functions
  6.7- documentation strings
  6.8- finction annotations
## 3]Data Structures--.
1. Using Lists as-
  1.1- stacks
  1.2- Queues
  1.3- List comprehensions
  1.4- nested List Comprehensions
2. The Del Statement
3. Tuples and Sequences
4. Sets
5. Dictionaries
6. Looping techniques
7. More on conditions
8. Comparing sequences and other types
## 4] Input and Output
1. Fancier output formatting-
  1.1- Formatted string Literals
  1.2- The String Format()method
  1.3- Manual String formating
  1.4- Old String Formatting
2. Reading and Writing Files-
  2.1- Methods of File Objects
## 5]Errors and Exception-->
1. Syntax Errors
2. Exceptions
3. Handling Exception
4. Raising Exception
5. User-Defined Exeption
## 6]Classes
1. Introduction to Name and Objects
2. Python scopes and naespaces
3. More on Classes-
  3.1- Class Definition Syntax
  3.2- Class objects
  3.3- instance objects
  3.4- method objects
  3.4- class and instance variables
4. Random remarks
5. Inheritance-
  5.1- self inheritance
  5.2- multiple inheritance
6. private variables
7. Iterators
8. generators
9. Generator expressions
## 7]Modules and Packages
1. Importing an other module into the current module
2. Importing  the required function from other module into current module

References-[Python resources 1](https://docs.python.org/3/tutorial/)
          -[Python resources 2](https://www.learnpython.org/)

# Python Libraries-
## Numpy -
1. Numpy Arrays-
  1.1- Creating arrays
  1.2- Basic data types
  1.3- Indexing and slicing
  1.4- copies and views
2. Numerical Operations on numpy arrays-
  2.1- elementwise operations
  2.2- basic reductions
  2.3- array shape manipulations
  2.4- sorting data
3. Advanced Operations
  3.1- polynomials
  3.2- Loading Data files(text files,images)
4. Exercises
  4.1- Image manipulation
  4.2- array manipulations
  4.3- Data statistics
   
References-[Numpy](https://scipy-lectures.org/intro/numpy/index.html)
  
  ## Matplotlib-
  1. Simple Plots
    (plotting with settings,changing colors and linewidths,setting ticks,limits,legend,etc.)
  2. Figures,Subplots,axes and ticks
  3. Other types of plots
    (regular plots,scatter plots,bar graph,pie chart,contour plots,imshow,,grids,3D plots,etc.)
    
 References- [Matplotlib](https://scipy-lectures.org/intro/matplotlib/index.html)
    
  ## Scipy-
  1. File Input//Output
  2. Special Functions
  3. linear algebra operations
  4. Interpolations
  5. optimization and fit
  6. Statistics and random numbers
  7. Numerical Integration
  8. Fast fourier transform
  9. Signal processing
  10. Image manipultion
  
  References-[Scipy](https://scipy-lectures.org/intro/scipy.html)
  
  
# Week-2-Progress
Documentation of what I have learnt int he week 30th March to 6th April 2020 

In this week ,an assignment was given which consisted of 4 questions based on python basics and python libraries namely
numpy ,scipy and matplotlib.

The question which I undertook was about denoising the image.There was an image with salt and pepper noise.The task was to minimize this noise.This was dine by the algorithm that they have mentioned.It included keeping record of black_count, white_count,mid_count,Mid_total and then recontructing final matrix.
There were many values of pixels for the single position.The challenge was how to asssign a particular value of pixel at that
particular position.Hence,in order to write this program,i wrote a code which included many functions of numpy.I learnt the use of conditions imposing through boolean values,use of a.any fuction,etc.

My teammates namely Ayush Shrivastava,Harsh Kumar,Nirmal Shah did the rest thre questions of assignment.Ankit kumar Jain helped me a lot for debugging in question 2.I thank him a lot.We all did the assignment very well.
I learnt a lot of good stuff during this week. 
 
# Week-3,4,5-progress
Documentation of what I have learned in the week 7th-12th,13th-19th,20th-26th April

## OpenCV
OpenCV is open source **computer vision** library.It supports C,C++,python,java on windows,max,Linux operating systems.
(_comuter vision is the way we teach intelligence to machines and making them see things just like humans.ex-self driving car_)
OpenCV helps in analyzing and manipulating images,videos,etc. through its inbuilt functions with help of numpy and matplotlib.

#### Two types of digital images-
1. Gray scale image(2D,gives light intensity at each pixel,one channel)
2. Coloured image(3D,3rd dimension is of colour,three channels namely R,G,B)

I have installed OpenCV's 4.2.0 version on my Ubuntu 18.04 with python version 3.6.9.
OpenCV stores images in form of B,G,R format but not in R,G,B format.

### Image Processing using opencv
1. **How to read,write images and videos from camera**
   ```
      cv2.imread()
      cv2.VideoCapture()
      cv2.videoWriter()
      cv2.imshow()
   ```
2. **Drawing Geometric Shapes on images**
   ```
      cv2.line(img,l_b,u_b,color,thickness)
      cv2.arrowedLine(img,l_b,u_b,color,thickness)
      cv2.rectangle(img,pt1,pt2,color,thickness)
      cv2.circle(img,center,radius,color,thickness)
      cv2.putText(img,text,org,font_face,font_size,font_color,thickness,line_type)
   ```
3. **Setting camera parametres**
4. **Show date and time on videos**
   ```
      import datatime
      datet=str(datatime.datatime.now())
      #then use cv2.putText to print
   ```
5. **Handling mouse events**
6. **Using split,merge,resize,add,addweighted,ROI**
   ```
      cv2.split() #spliting b,g,r channels of coloured images
      cv2.merge() #merging b,g,r channels of splitted image
      cv2.add(img1,img2)
      cv2.resize(src,size)
      cv2.addWeighted(img1,wt1,img2,wt2,const)
   ```
7. **Bitwise Operators**
   ```
      cv2.bitwise_and(img1,img2)
      cv2.bitwise_or(img1,img2)
      cv2.bitwise_not(img)
      cv2.bitwise_xor(img1,img2)
   ```
8. **Binding trackbars** 
   ```
      cv2.namedWindow()
      cv2.creatTrackbar(trackbar_name,img,lower_b,upper_b,function)
      cv2.getTrackbarPos(trackbar_name,img)
   ```
9. **Object Detecion and object tracking using hsv color space**
   ```
      l_b=np.array([l_h,l_s,l_v])
      u_b=np.array([u_h,u_s,u_v])
      mask=cv2.inRange(img,l_b,u_b)
      res=cv2.bitwise_and(frame,frame,mask=mask)
   ```
10. **Simple Image Thresholding**
   ```
      _,th1=cv2.threshold(img,threshold_value,max_value,threshold_type)
      #threshold types-cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
   ```
11. **Adaptive Thresholding**
   ```
      #thresholding for smaller regions
      cv2.adaptiveThreshold(src,max_value,adaptive_method,threshold_type,blocksize,const)
   ```
12. **Matplotlib using opencv**
13. **Morpholigical Transformations**
   ```
      cv2.dilate(mask,kernel,iteration)
      cv2.erode(mask,kernel,iteration)
      cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)  #erosion followed by dilation 
      cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #dilation followed by erosion
   ```
14. **Smoothing and Blurring images**
   ```
      #homogenous filter,gaussian filter,mean filter,bilateral filter
      cv2.filter2D(img,depth,kernel)
      cv2.blur(img,kernel_size)
      cv2.GaussianBlur(img,kernel_size,sigma_x_value)
      cv2.medianBlur(img,kernel_size)
   ```
15. **Image Gradients and edge detection**
   ```
      cv2.Laplacian(img,datatype,kernel_size)
      cv2.Sobel(img,datatype,1,0)  #sobel x
      cv2.Sobel(img,datatype,0,1)  #sobel y
   ```
16. **Canny Edge Detection**
   ```
      cv2.Canny(img,thresh1,thresh2)  #two threshold values for last step hysterisis
   ```
17. **Image Pyramids**
   ```
      #two kinds of image pyramids-gaussian and laplacian
      cv2.pyrDown(img)
      cv2.pyrUp(img)
   ```
18. **Image Blending**
   ```
      #load the two desired images
      #Form the Gaussian pyramids of two images upto some level,say 6.
      #From Gaussian,form Laplacian pyramids
      #Join the right and left half of each level of Laplacian pyramids
      #Reconstruct the original image
   ```
19. **Finding and Drawing Contours**
   ```
      contours,hierarchy=cv2.FindContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
      cv2.drawContours(img,contours,index,color,thickness)
   ```
20. **Motion Detection and Tracking**
21. **Detect Simple Geometric shapes**
   ```
      approx=cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
      cv2.boundingRect(approx)
   ```
22. **Understanding Image Histograms**
   ```
      b,g,r=cv2.cv2.split(img)
      plt.hist(b.ravel(),256,[0,256])
      plt.hist(g.ravel(),256,[0,256])
      plt.hist(r.ravel(),256,[0,256])
   ```
23. **Template Matching**
   ```
      w, h = template.shape[::-1]  
      res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
   ```
24. **Hough Line Transform using Hough Line Method**
   [Understand here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/29.%20%5BAnkit          %5D%20Hough%20Line%20Transform%20using%20HoughLines%20method%20.md)
   
25. **Probabilistic Hough Line Transform using Hough Line Method**
   [Understand here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/30.%20%5BAnkit%5D%20Probabilistic%20Hough%20Transform%20using%20HoughLinesP.md)
   
26. **Road Lane Line Detection**
27. **Circle Detection**
   ```
      cv2.HoughCircles(img,detection method,dp,min_dist,parameter1,parameter2,minRadius,maxRadius)
      detected_circles = np.uint16(np.around(circles))
   ```
28. **Face Detection**
   ```
      face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
      faces = face_cascade.detectMultiScale(gray, scale_factor,min_neighbours)
   ```
29. **Eye Detection**
   ```
      eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') 
      eyes = eye_cascade.detectMultiScale(roi_gray)
   ```
30. **Detect Corners using Harris Corner Detect method**
   ```
      cv2.cornerHarris(img,block_size,k_size,harris_param)
   ```
31. **Detect Corners using shi Tomasi method**
   ```
      corners = cv.goodFeaturesToTrack(img,no_of_corners,quality,Euclidean_distance)
   ```
32. **Background subtraction** 
      [Understand Here](https://www.youtube.com/watch?v=eZ2kDurOodI&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=43)

_References_-
[OpenCV_GitHub](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/tree/master/SoC_OpenCV-master)
[OpenCV_youtube](https://www.youtube.com/playlist?list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
      
## Sudoku Assignment-
   The main aim was to find the solution of a given sudoku just by reading the given sudoku image.
   Following steps were implemented in the code in **preprocessing**-
   1. Detection of max. area contour i.e. sudoku's 9x9 square.
   2. Performing Perspective transform.
   4. Detection of individual 81 squares and storing into another array.
   5. Reducing noise i.e.unwanted pixels.
   
   Digit recognition and finding solutions to the sudoku is to be done by neural networks(ML part).
                  
## VIRTUAL KEYBOARD-
   Following Steps are performed in the code-

   1. Reading of video.
   2. Performing perspective transform and getting max.area which is assumed to be of keyboard.
   3. reducing noise.
   3. Background Subtraction and thresholding hand's frame.
   4. Detecting topmost tip of finger.
   5. Detecting whether the key is presssed or not.
   6. Checking whether the key is capslock or not
   7. Typing text on frame according to lower_case or upper_case.
