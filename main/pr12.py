#!/usr/bin/env python3

import cv2
import numpy as np
import os

# Load the background image
background = cv2.imread('pexels-padrinan-255379.jpg')

# Define the color to change white objects to (e.g., blue)
new_color = [255, 0, 0]

# Create an output directory for processed frames
if not os.path.exists('processed_frames'):
    os.makedirs('processed_frames')

# Loop through each frame
frame_files = sorted([f for f in os.listdir('frames') if f.endswith('.png')])
for frame_file in frame_files:
    # Read the frame
    frame = cv2.imread(os.path.join('frames', frame_file))

    # Create a mask for white objects
    white_mask = cv2.inRange(frame, np.array([200, 200, 200]), np.array([255, 255, 255]))
    
    # Change white objects to the new color
    frame[white_mask == 255] = new_color

    # Create a mask for the character and objects (excluding the background)
    bg_mask = cv2.bitwise_not(white_mask)
    fg = cv2.bitwise_and(frame, frame, mask=bg_mask)

    # Resize background to match frame size
    bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    # Combine foreground (character and objects) with the new background
    combined = cv2.add(fg, cv2.bitwise_and(bg_resized, bg_resized, mask=white_mask))

    # Save the processed frame
    cv2.imwrite(os.path.join('processed_frames', frame_file), combined)

print("Frame processing complete.")

