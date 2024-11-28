#!/usr/bin/env python3

import cv2

# Открываем видеофайл
cap = cv2.VideoCapture('output_video.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Читаем и отображаем кадры видео
while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    cv2.imshow('Video', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Освобождаем объект захвата и закрываем окна
cap.release()
cv2.destroyAllWindows()

