# Virtual Keyboard - Progress Report

## Week 1
* **Dual boot PC with Ubuntu 18.04**
    - A video regarding dual boot was shared with us, and it seemed I might be able to do it easily.But, it turned out that Ubuntu doesn't support Optane Memory, which was the case with me.
    - But, internet holds the solution too and I got [this video](https://www.youtube.com/watch?v=2uXgbF3P2F8&list=WL&index=12&t=149s) which finally helped me dual boot my system with ubuntu
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
I had a github account but never did I use it. So, I saw the guide about basic operations which is already there on every Github page.

* **Learn basics of Markdown file**
- These are text files which have text formatting feature like headings, bold text, tables, code blocks, etc.
- You will find it on most of the Github repos(the files with extension .md). These are very good proper documentation of a repo.
- [This cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides all things needed to start writing a markdown file

* **Ubuntu Terminal**
    - By far the best thing I've ever used! It is an interface which lets you do literalyy anything by typing a few commands, isn't that amazing!
    - Also, there are a lot of resources to learn it. [This cheatsheet](https://github.com/iamshm/Linux-Unix-Commands/blob/master/Commands.md) just sums up everything.
    - Oh! Ever tried installing codeblocks in Windows, its literally a pain for beginners, but try installing it in Ubuntu!!!

* **Learn python**  
Our mentor handed us a lot of python resources. Reading them takes time but when your code runs.... What a satisfaction!
Other than the bascics of python, there were resources for frequently used python libraries too.
    1. [Resource1](https://docs.python.org/3/tutorial/) and [Resource2](https://www.learnpython.org/) have a lot of similar things from basics to advance programming.
    2. [Python Scipy](https://scipy-lectures.org/) is also a good ML library.

## Week 2
* **Get familiar with Python**  
As I was learning python for the first time, it was important to practice it and familiarize with it. And to solve some coding problems, HackerRank is a good option.

* **Assisgnment1**  
    - We were divided into teams of 4 and we had to complete the first assisgnment. It had 4 problems, 1 for each member.
    - I was doing [this task](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Assignment%201/Team%206/AkshatVira_Problem_2.py)
    - After completing the task, I went through most of the codes that were written by other mentees & mentor too, and actually I got to learn very different approaches, commenting styles and how to write good explanations.


## Week 3
* **OpenCV Tutorials**  
Opencv is one of the most widely used Computer vision library. It has a lot of features.  
The resouces used were [OpenCV Video Tutorials](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) and [OpenCV GFG Tutorials](https://www.geeksforgeeks.org/opencv-python-tutorial/)


## Week 4
* **Document OpenCV Tutorial**  
We had to document a couple of OpenCV tutorials that were given to us.  

I had worked on [Face Detection](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/35.%20(Akshat)%20Face%20Detection%20using%20Haar%20Cascade%20Classifiers.md) and [Eye Detection](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/36.%20(Akshat)%20Eye%20Detection%20Haar%20Feature%20based%20Cascade%20Classifiers.md)

## Week 5
* **Invisibility Cloak**  
This project was very interesting. This was kinda direct application of what we learnt in previous weeks. [Here](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Invisibility%20Cloak/Akshat.md) is my try.

* **Ubuntu issues**  
1. I got the error 'UNEXPECTED INCONSISTENCY: Run fsck MANUALLY' while booting into Ubuntu.
I blindly followed some tricks from internet and ubuntu booted successfully... but, I wasn't able to open terminal, software update center & chrome was uninstalled... And I was doomed.
2. I rebooted the system, and now it boots into emergency mode and I'm stuck in it.
3. After discussing a lot and finding solutions on google, I finally decided to uninstall ubuntu(Didn't take the risk of reinstalling as my laptop might require some other process than the one shown on youtube)
    
* **Conclusion**  
1. Do not blindly follow online solutions.
2. Find the reason behind the error, discuss with some senior and then apply it.
3. **Do not run fsck on mounted filesystems**(Yes, I did that!)
