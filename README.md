## Overview
Realtime Feedback Application

Use open cv to detect the active speaker based on the Google meet captions.
### How it works:
-First ask two people you want to detect as speakers to change their google account profile pictires to solid colors (Red and Green here).
-Active captions of google meet
-Program would use OpenCv to record your screen and the algorithem, would detect the active speaker per frame (frame=one second).
-After three successful taking turn base on the set threshold(you can change the threshold in the code)between two speaking poeple you would here the song as the feedback. 


## Sample example
![TurnTakingApplication](https://user-images.githubusercontent.com/60202851/101586121-90f2d880-3a24-11eb-8444-414cbc092770.JPG)


### Dependencies:
* pip install opencv-python
* pip install numpy
* pip install pyautogui
* pip3 install threading



### Note: You need to make a folder with the name Unknown so that python with save the screen shots temprary


### Usage:
First make a folder with the name Unknown so that python with save the screen shots temprary.
Then put the song.mp3 (or any song file of prefrence in the correct folder## don't forgoet to change the song in the code as well)
Then run turn-taking.py

### Acknowledgements:

