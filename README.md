# SOC_20 Virtual Keyboard


This is a project I'am mentoring along with Parth Laturia (https://github.com/ParthLa) as a part of Seasons of Code, WnCC IITB.

![manan-keyboard](https://user-images.githubusercontent.com/62146744/77977952-75282600-731e-11ea-8af9-4ec8a559eff3.jpeg)


The project is about making a virtual keyboard that can be projected on any flat surface like a table and then can be used to type in real-time. To start with, we need to program image processing that senses touch at a certain key on the virtual setting of keyboard.This can be achieved by detecting and locating the center position of the light outline to discern and detect the position of finger and then map to keyboard position to achieve relative keyboard key events.

With OpenCV vision library, it is fast to find the finger outline which is get by image camera, the position of finger location and revise the image surface distortion which is caused by image camera.

After that, our task would be to fetch programs for individual as well as combination of keys (ex. Shift + any letter = Capital).

This project is also a little hardware intensive along with the software part as proper calibration, correct positioning of different components and code testing needs to be done at various steps. Hardware testing shall be done by the mentors and mentees who would be in the insti during the summer vacations and the results and changes would be shared with those at home.














