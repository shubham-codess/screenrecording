from datetime import datetime
import imp
from time import strftime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

# Get max height and width of the screen.
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Dynamic File Name recorded as time stamp.
time_stamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
print(time_stamp)

# Encoding video catured in mp4.
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
recorded = cv2.VideoWriter(file_name,fourcc, 20.0,(width,height))

# Grabbing Image, converting color, writing images to video untill pressed "q" to quit.

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("test", img_final)
    recorded.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break

# Made With Love. --Shubham Varshney
