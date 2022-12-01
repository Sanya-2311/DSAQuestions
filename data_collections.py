"""import mediapipe as mp
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

name = input("Enter the name of the data : ")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.draw_utils

x=[]
data_size=0

while True :
    lst = []

    _, frm = cap.read()

    frm = cv2.flip(frm, 1)

    res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))


    if res.face_landmarks : 
        for i in res.face_landmarks.landmark:
            lst.append(i.x-res.face_landmarks.landmark[1].x)
            lst.append(i.y-res.face_landmarks.landmark[1].y)
        if res.left_hand_landmarks.landmark:
            lst.append(i.x-res_left_hand_landmarks.landmark[8].x)
            lst.append(i.y
            -res_left_hand_landmarks.landmark[8].y)"""
