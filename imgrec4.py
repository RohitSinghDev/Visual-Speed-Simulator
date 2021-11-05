import time
import pyautogui

import cv2

import pickle
import os
import matplotlib.pyplot as plt
import numpy as np
import skimage
import sklearn
from skimage.io import imread
from skimage.transform import resize


def predict():
    CATEGORIES = ["green_traffic_signal", "red_traffic_signal", "slow_road_sign", "stop_traffic_sign"]

    model = pickle.load(open('img_model.p', "rb"))
    flat_data = []
    url = "opencv_frame_0.png"
    img = imread(url)
    img_resized = resize(img, (150, 150, 3))
    flat_data.append(img_resized.flatten())
    y_out = model.predict(flat_data)
    return CATEGORIES[y_out[0]]


def camera3():
    done = 0
    camera1 = cv2.VideoCapture(0)
    cv2.namedWindow("traffic sign")

    while True:
        ret, frame = camera1.read()
        if not ret:
            print("Done")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("closed")
            done=1
            break
        elif k % 256 == 32:
            img_name = "opencv_frame_0.png"
            cv2.imwrite(img_name, frame)
            print("taken")

            camera1.release()
            cv2.destroyAllWindows()
    camera1.release()
    cv2.destroyAllWindows()
    return done

boolean = True

while boolean:
    done_check = camera3()
    time.sleep(5)
    pyautogui.press("space")
    speed = int(input("enter speed: "))
    signal = 0
    check = predict()
    if check == "green_traffic_signal":
        print("green")
        signal = 0
    elif check == "red_traffic_signal":
        print("red signal")
        signal = 1
    elif check == "slow_road_sign":
        print("slow down")
        signal = 2
    elif check == "stop_traffic_sign":
        print("stop")
        signal = 3
    else:
        signal = 4

    if signal == 1 and speed > 0:
        while speed > 0:
            print(speed, "....")
            speed -= 5
            time.sleep(0.3)
        if speed != 0:
            speed = 0
            print(speed)
    elif signal == 2 and speed > 30:
        while speed > 30:
            speed -= 2
            print(speed, "...")
            time.sleep(0.3)
    elif signal == 3 and speed > 0:
        while speed > 0:
            print(speed, "...")
            speed -= 8
            time.sleep(0.3)
        if speed != 0:
            speed = 0
            print(speed)


    if done_check == 1:
        boolean = False


