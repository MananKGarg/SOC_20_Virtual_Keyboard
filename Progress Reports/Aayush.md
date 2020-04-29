# Virtual Keyboard
_Aayush Shrivastava_

## Week 1 (First four Days)
Learned about Github like how to create a repo, make a branch, commit changes and merge to master branch.

How to dual boot and install ubuntu and use various linux commands.

How to edit markdown(.md) files
    
**Notes** (Markdown File)
    
* (#) for heading
* _ or * (withoutspace) for Italics
*  ** for bold
* for ordered listing simply use numbers
* use * for unordered listing
* use ~~ for text with cut
* for adding Links we can use [] where inside square brackets comes the name which will show on the link then comes () inside this comes the link. If we want to add like if someone hovers over the link then show some text then we can add text in " " that need to be displayed inside the brackets after the link with a space.
* similarly for adding images just add ! before in the link procedure.
* To write any piece of code with higlighting use three aposhtrophe signs(') then the programming language and you must end with three aphostrophe signs when you are finished with your code.
* to add any quotes use > sign.
* we can use three dash or three astreick signs to add horizontal line    
* [For more tricks](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)

---

## Week 1 (last three days)

>Learning python programming language

first 2 days were reading the python official [documentation](https://docs.python.org/3/tutorial/index.html) the topics included -
1. basic data types like lists strings and expressions using python IDLE.
2. Read about control flow tools.
     - if, else and elif statements and their syntax
     - for and while loops
     - defining functions and other useful functions
3. The various data structures
     - using lists as stack, queue.
     - list comprehensions.
     - tuples, sets and dictionaries
     - looping techniques
4. Reading about formatting output and reading and writing data from a file.
5. Errors and exception handling which include try, except and raise statements.
6. Object Oriented proframming
     - classes and instances 
     - inheritance
     - Private variables 
     - generators and iterators

Next we have to go through the basics, data science tutorials and advanced tutorials(first half) from this [site](https://www.learnpython.org/) which covered the bascis of python, numpy and a bit of panda.
In the last from this [site](https://scipy-lectures.org/) covered the first topic which included intro to important libraries of python like numpy, matplotlib and scipy.

The last two sites were advanced and long so it extended to mid of next week.

## Week 2

In this week Our major focus was on the Assignment which was assigned as a team of 4. The assignment consisted of four problems in which each member has to one problem.
I did the 4th problem.
Most of the time was spent in debugging as problem asked for implementing code without loops of inbuilt functions.
Also practiced some questions on [Hackerrank](https://www.hackerrank.com/domains/python).

## Week 3

In this week the first two days were kept to the solutions of the assignment and submission of other teams solution.

Then we started Image Processing with OpenCV library of python from these [video](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) tutorials and from [these](https://www.geeksforgeeks.org/opencv-python-tutorial/).

During these tutorials we came to know various things about images and how they are handeled.
Images consist of pixels whose values are stored in arrays. Grayscale images are 2D array in which the value at a position gives the intensity of the pixel at that location. Colored images have 3 channels BGR in openCV, then it is a 3D array in which each channel's 2D matrix contains the intensity of that particular color.

During this week we were also told to practice questions of python on Hackerrank to get more grip on the language.

## Week4

In this week first few days we completed the geekforgeeks tutorials on openCV and then we were asked to make notes of openCV video tutorials we watched.
The video tutorials consisted of total 41 videos having various algos, functions and concepts which we can't remember only just by watching the videos.
So we made our own notes in the GitHub repo each indiviual were given to choose two videos from the tutorial write the concept, function used and heavily comment the code used in the video.
The notes we created are [here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/tree/master/SoC_OpenCV-master)

After that we were given an indiviual project.
The project consisted of creating the invisiblity cloak of Harry Potter using openCV.

The project was fun and it included the following steps:-
1. Capture and store the background frame.
2. Detect the red colored cloth using color detection algorithm.
3. Segment out the red colored cloth by generating a mask.
4. Generate the final augmented output to create the magical effect

The project took around 3-4 days to complete as segmenting the cloth of our choice color required time to find and calibrate the HSV values and figuring out how to show background once cloth was detected.
The project code was easily available on the internet but our mentor asked us do everything from scracth so that we learn more.
The code of my project is [here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Invisibility%20Cloak/Aayush.md)
