## Overview
Realtime Feedback Application

Use open cv to detect the active speaker based on the Google meet captions.
### how it works:
-First ask two people you want to detect as speakers to change their google account profile pictires to solid colors (Red and Green here).
-Active captions of google meet
-Program would use OpenCv to record your screen and the algorithem, would detect the active speaker per frame (frame=one second).
-after three successful taking turn base on the set threshold(you can change the threshold in the code)between two speaking poeple you would here the song as the feedback. 


## Sample example
https://youtu.be/DtBu1u5aBsc

### Dependencies:
* pip install numpy
* pip install pandas
* pip install tensorflow
* pip install keras
* pip install opencv-python

Download haarcascades file from here=> https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

### Note: You need to make a folder with the name Unknown so that python with save the screen shots temprary
http://www.mediafire.com/folder/trbjv7bysiycl/challenges-in-representation-learning-facial-expression-recognition-challenge

### Usage:
First make a folder with the name Unknown so that python with save the screen shots temprary.
Then put the song.mp3 (or any song file of prefrence in the correct folder## don't forgoet to change the song in the code as well)
Then run turn-taking.py

### Acknowledgements:

