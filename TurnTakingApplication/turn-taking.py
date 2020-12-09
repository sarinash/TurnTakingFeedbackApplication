import threading
import time
from threading import Timer
import cv2
import numpy as np
import pyautogui
import csv
import datetime
import playsound
from numpy import mean

##################################################################################################################


fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
PersonRed = []
PersonGreen = []
RedArray = []
GreenArray = []
TurnTakingArrayRed = []
TurnTakingArrayGreen = []


# R = 1  # counter for person red talking in seconds within twenty seconds
# G = 1  # counter for person green talking in seconds within twenty seconds


##########################################################################################3
def record_Screen(epoch):  # record screen every two seconds
    # create the video write object
    out = cv2.VideoWriter('C:/Users/sarina/Desktop/unknown/' + str(epoch) + '.avi', fourcc, 8.0, (90, 120))
    for s in range(15):  # 15 is two seconds
        # make a screenshot
        img = pyautogui.screenshot(region=(350, 840, 90, 120))  # this region belongs to comments in Google meet
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        cv2.imshow("screenshot", frame)
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break
        # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()
    # threading.Timer(2, record_Screen).start()


##########################################################################################3
# function to mask the two people by color coding or red and green
def speaker_recognization(epoch):
    cap = cv2.VideoCapture('C:/Users/sarina/Desktop/unknown/' + str(epoch) + '.avi')
    RedT = 0
    GreenT = 0
    BlueT = 0

    for j in range(15):
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Red color
        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)
        # Blue color
        # low_blue = np.array([94, 80, 2])
        # high_blue = np.array([126, 255, 255])
        # blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        # blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        # Green color
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        # cv2.imshow("Frame", frame)
        # cv2.imshow("Red", red)
        # cv2.imshow("Blue", blue)

        RedT = RedT + np.mean(red_mask)
        GreenT = GreenT + np.mean(green_mask)
        # BlueT = BlueT + np.mean(blue_mask)
        PersonRed.append(RedT)
        PersonGreen.append(GreenT)

        # if RedT < 100 and BlueT < 100:
        #     print("none of them are speaking")
        # else:
        #     if RedT / BlueT > 10:  # 10 should be fixed and is a guess now
        #         print("person red speaks much more ")
        #     elif BlueT / RedT > 10:
        #         print("person blue speaks much more")
        #     else:
        #         print("two of them spoke in an appropriate time")

        # cv2.imshow("Blue", blue)
        # cv2.imshow("Green", green)

        key = cv2.waitKey(1)
        if key == 27:
            break


########################################################################################

# play function for happy

def play():
    playsound.playsound('song.mp3', True)


def start_play():
    w = threading.Thread(name='thread_play', target=play)
    w.start()


########################################################################################

# play function for sad

def play_sad():
    playsound.playsound('sad.mp3', True)


def start_play_sad():
    ww = threading.Thread(name='thread_play_sad', target=play_sad)
    ww.start()


##################################################################################################################
# run the code

for i in range(1, 100000000):
    RedSpeaking = 0
    GreenSpeaking = 0

    currentTime = time.time()
    Time = datetime.datetime.now()

    epoch = int(round(currentTime * 1000))
    record_Screen(epoch)
    speaker_recognization(epoch)

    ###################################################################################################
    # Conditioning over who is speaking after each second:
    if PersonRed[len(PersonRed) - 1] > 100 and PersonGreen[len(PersonGreen) - 1] < 200:
        print(Time, "red is speaking")
        RedSpeaking = 1
        # R += 1
    elif PersonGreen[len(PersonGreen) - 1] > 100 and PersonRed[len(PersonRed) - 1] < 200:
        print(Time, "green is speaking")
        GreenSpeaking = 1
        # G += 1
    elif PersonGreen[len(PersonGreen) - 1] == 0 and PersonRed[len(PersonRed) - 1] != 0:
        print(Time, "red is speaking")
        print("lalala")
        RedSpeaking = 1

    elif PersonGreen[len(PersonGreen) - 1] != 0 and PersonRed[len(PersonRed) - 1] == 0:
        print(Time, "green is speaking")
        print("lalala")
        GreenSpeaking = 1


    elif PersonGreen[len(PersonGreen) - 1] > 30 and PersonRed[len(PersonRed) - 1] > 30:
        if (PersonGreen[len(PersonRed) - 1] > 600 and PersonRed[len(PersonGreen) - 1] != 0) or (
                PersonGreen[len(PersonRed) - 1] - PersonRed[len(PersonRed) - 1]) > 10:
            print(Time, "red is speaking")
            print("hahah")
            RedSpeaking = 1

        elif (PersonRed[len(PersonGreen) - 1] > 600 and PersonGreen[len(PersonGreen) - 1] != 0) or (
                PersonRed[len(PersonRed) - 1] - PersonGreen[len(PersonRed) - 1]) > 10:
            print(Time, "green is speaking")
            print("me")
            GreenSpeaking = 1

        else:
            print(Time, "both are speaking now")
            RedSpeaking = 1
            GreenSpeaking = 1


    else:
        print(Time, "none are speaking now ")
    RedArray.append(RedSpeaking)
    GreenArray.append(GreenSpeaking)
    ############################################################################################################
    # condition for feedback:
    if i % 40 == 0 and i != 0:
        print(RedArray)
        print(GreenArray)
        indexesRed = [index for index in range(len(RedArray)) if RedArray[index] == 1]
        indexesGreen = [index for index in range(len(GreenArray)) if GreenArray[index] == 1]
        print(indexesRed)
        print(indexesGreen)
        for j in indexesRed:
            if RedArray[j - 1] == 0 and RedArray[j - 2] == 0:
                TurnTakingRed = sum((GreenArray[j - 5:j])) + sum((GreenArray[j - 4:j])) + sum((GreenArray[j - 3:j])) + sum(
                    (GreenArray[j - 2:j])) + sum(GreenArray[j - 1:j])
                if TurnTakingRed > 0:
                    TurnTakingRed = 1
                TurnTakingArrayRed.append(TurnTakingRed)
                print(TurnTakingArrayRed)
        print(sum(TurnTakingArrayRed))
        for j in indexesGreen:
            if GreenArray[j - 1] == 0:
                TurnTakingGreen = sum((RedArray[j - 5:j])) + sum((RedArray[j - 4:j])) + sum((RedArray[j - 3:j])) + sum(
                    (RedArray[j - 2:j])) + sum(RedArray[j - 1:j])
                if TurnTakingGreen > 0:
                    TurnTakingGreen = 1
                TurnTakingArrayGreen.append(TurnTakingGreen)
                print(TurnTakingArrayGreen)
        print(sum(TurnTakingArrayGreen))
        TotalTurnTaking = sum(TurnTakingArrayRed) + sum(TurnTakingArrayRed)
        if TotalTurnTaking > 2:
            start_play()
        # GreenTurnTaking = sum(map(lambda pair: pair[0] * pair[1], zip(RedArray, GreenArray[1:len(GreenArray)])))
        # RedTurnTaking = sum(map(lambda pair: pair[0] * pair[1], zip(RedArray[1:len(RedArray)], GreenArray)))
        # TurnTaking = RedTurnTaking + GreenTurnTaking
        # print(GreenTurnTaking)
        # print(RedTurnTaking)
        # print(TurnTaking)
        # if TurnTaking>3:
        # start_play()

        # print(PersonRed)
        # print(PersonGreen)
        # print(mean(PersonGreen[(Size - 300): (Size + 1)]))
        # print(mean(PersonRed[(Size - 300): (Size + 1)]))

        # PersonRed_Total = mean(PersonRed[(Size - 300): (Size + 1)])
        # PersonGreen_Total = mean(PersonGreen[(Size - 300): (Size + 1)])
        # print('Seconds Red was talking', R)
        # print('Seconds Green was talking', G)
        # if (PersonRed_Total - PersonGreen_Total) > 126:
        #     print(Time, "red was speaking more in the last 20 seconds")
        #
        # elif (PersonGreen_Total - PersonRed_Total) > 154:
        #     print(Time, "green was speaking more in the last 20 seconds")
        #
        # elif PersonRed_Total and PersonGreen_Total < 100:
        #
        #     print(Time, "none were speaking enough ")
        #     # start_play()
        #     start_play_sad()
        #
        # else:
        #     print(Time, "both were speaking ")
        #     start_play()

        # if (G + R) < 10:
        #     print(Time, "none were speaking enough ")
        #     start_play_sad()
        # elif G / R > 3:
        #     print(Time, "green was speaking more in the last 20 seconds")
        # elif R / G > 3:
        #     print(Time, "red was speaking more in the last 20 seconds")
        #
        # else:
        #     print(Time, "both were speaking ")
        #     start_play()

        # R = 1
        # G = 1
        RedArray = []
        GreenArray = []
        TurnTakingArrayRed = []
        TurnTakingArrayGreen = []

    ############################################################################################################
    # save data to csv
    with open('C:/Users/sarina/Desktop/csv1.csv', 'a', newline='') as csvfile:
        filednames = ['Time', 'RedT', 'GreenT']
        thewriter = csv.DictWriter(csvfile, fieldnames=filednames)
        # thewriter.writeheader()
        for k in range(len(PersonRed) - 1, len(PersonRed)):
            # print(len(PersonRed))
            thewriter.writerow(
                {'Time': Time, 'RedT': PersonRed[len(PersonRed) - 1], 'GreenT': PersonGreen[len(PersonGreen) - 1]})
