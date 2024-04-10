import cv2 
import pandas as pd
import numpy as np
from ultralytics import YOLO
import pickle


# model = YOLO('yolov8s.pt')

# with open('model.pkl','wb') as f:
#     pickle.dump(model,f)

with open('model.pkl','rb') as f:
    model = pickle.load(f)

# print(model)

cap = cv2.VideoCapture('highway_mini.mp4')

while True:
    sucess,frame = cap.read()
    frame = cv2.resize(frame,(450,550))
    # results = model.predict(frame,show=True)
    results = model.predict(frame)
    a = results[0].boxes.data
    a_cpu = a.cpu()
    px = pd.DataFrame(a_cpu.numpy()).astype("float")
    for index,row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
        


    cv2.imshow('frame',frame)
    if cv2.waitKey(0) and 0xFF==27:
        break

cap.release()

cv2.destroyAllWindows()