# Virtual Keyboard - Progress Report

## Task 1
* **Dual boot PC with Ubuntu 18.04**
> **Reason to use Ubuntu**: Ubuntu would be a necessity second year onwards and Ubuntu has a lot of advantages in programming and software dev  

  - A video regarding dual boot was shared with us, and it seemed I might be able to do it easily.But, it turned out that Ubuntu doesn't support Optane Memory, which was the case with me.
  - But, internet holds the solution too and I got [this video](https://youtu.be/2uXgbF3P2F8), which finally helped me dual boot my system with ubuntu
The problem doesn't end here, each time the system is updated you have to follow some steps:  
(Got this from the comments of same video.)  
      1. Disable optane from windows  
      2. Switch to AHCI  
      3. Go to ubuntu via chroot (via Live USB) or boot from an older kernel  
      4. Run "sudo update-initramfs && update-grub"  
      5. Switch back to RST Optane  
      6. Enable Optane on Windows  

> P.S: **Although, simply switching to AHCI in BIOS can solve this without following the above steps.**

* **Learn Github**  
> **Reason to use**: It is a very good tool for version management   

I had a github account but never did I use it. So, I saw the guide about basic operations which is already there on every Github page and started using it.

* **Learn basics of Markdown file**
    - These are text files which have text formatting feature like headings, bold text, tables, code blocks, etc.
    - You will find it on most of the Github repos(the files with extension .md). These are very good proper documentation of a repo.
    - [This cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides all things needed to start writing a markdown file

* **Ubuntu Terminal**
    - The most interesting part of ubuntu. It is an interface which lets you do literaly anything by typing a few commands, isn't that amazing!
    - Also, there are a lot of resources to learn it. [This cheatsheet](https://github.com/iamshm/Linux-Unix-Commands/blob/master/Commands.md) just sums up everything.
    - Installing software or coding in python or creating files, this terminal can do anything!

* **Learn python**  
Our mentor handed us a lot of python resources. Reading them takes time but when your code runs.... What a satisfaction!
Other than the bascics of python, there were resources for frequently used python libraries too.
    1. [Resource1](https://docs.python.org/3/tutorial/) and [Resource2](https://www.learnpython.org/) have a lot of similar things from basics to advance programming.
    2. [Python Scipy](https://scipy-lectures.org/) is also a good ML library.

## Task 2
* **Assisgnment1**  
    - We were divided into teams of 4 and we had to complete the first assisgnment. It had 4 problems, 1 for each member.
    - I was doing [this task](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Assignment%201/Team%206/AkshatVira_Problem_2.py)
    - After completing the task, I went through most of the codes that were written by other mentees & mentor too, and actually I got to learn very different approaches, commenting styles and how to write good explanations.  
* **Learnings:**
- Basic uses of python
- Image reconstruction
- K Clustering


## Task 3
* **OpenCV Tutorials**  
Opencv is one of the most widely used Computer vision library. It has a lot of features like object detection, facial recognition, optical character recognition, image processing and a whole lot more  
* **What I learned:**
    - Basic Image processing
    - Edge detection, hough lines transform
    - Face, eye detection
    - Template matching
and much more.  

* **Resources**
    - [OpenCV Video Tutorials](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
    - [OpenCV GFG Tutorials](https://www.geeksforgeeks.org/opencv-python-tutorial/)  


## Task 4
* **Document OpenCV Tutorial**  
In this task, We had to document a couple of OpenCV tutorials that were given to us so that we have a record of what we learned and use it as a reference anytime when we need it in future  
I had worked on [Face Detection](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/35.%20(Akshat)%20Face%20Detection%20using%20Haar%20Cascade%20Classifiers.md) and [Eye Detection](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/36.%20(Akshat)%20Eye%20Detection%20Haar%20Feature%20based%20Cascade%20Classifiers.md)

## Task 5
* **Invisibility Cloak**  
This project was very interesting. We had to make a code for an invisibility cloak which was used in Harry Potter. This was kinda direct application of what we learnt in previous weeks.[Here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Invisibility%20Cloak/Akshat.md) is my try. Take a look at this [video](https://drive.google.com/drive/folders/1TfShKmjxdlR3CUne1xtNW6aYwMUwHq8C?usp=sharing) too!  
* ** What I learned from this**
    - Image segmentation
    - HSV color space and its importance


## Task 6
* **Sudoku Solver**  
This was a tough one. We had to use image processing and ML to recognize and solve a sudoku grid. I was able to do the OpenCV part, however, the digit recognition(ML part) was quite difficult and I wasn't able to recognize digits properly.  
* **Learnings**
    - Perspective shifting
    - Digit extraction(optical character recognition)
    - Algorithm to solve sudoku

## Task 7
* **Paper Keyboard**  
This is the final aim of our project, to make a working virtual keyboard. So, we had to make a code which uses visual input of a pointer and keyboard and type the letters which are pointed on the paper keyboard. Also, every concept used in this code was very nicely covered in all the previous sub-project which made this code/project very intuitive and easy to go ahead with.
You can see the [code](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Paper%20Keyboard/Akshat.md) and its [implementation](https://drive.google.com/drive/folders/1TfShKmjxdlR3CUne1xtNW6aYwMUwHq8C?usp=sharing)  

------------  

So, this was a very good experience for me, I learned a lot of things and got to know the scope, the applications and the fun in using computer vision. This project also turned me from hating python to loving it. Moreover, this project has shown me what all can be done using computer vision and I would definitely explore this field further more.  
**Thanks a lot for selecting me as a part of this project!**
