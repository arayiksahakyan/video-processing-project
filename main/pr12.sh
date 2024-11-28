#!/bin/bash

# Check if input video file exists
if [ ! -f "bad_apple.mp4" ]; then
    echo "Input video file 'input_video.mp4' not found!"
    exit 1
fi

# Check if Python script exists
if [ ! -f "pr12.py" ]; then
    echo "Python script 'pr12.py' not found!"
    exit 1
fi

# Check if necessary Python libraries are installed
echo "Checking for required Python libraries..."

# Check if OpenCV (cv2) is installed
python3 -c "import cv2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "OpenCV (cv2) not found. Installing..."
    pip install opencv-python
fi

# Check if NumPy is installed
python3 -c "import numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "NumPy not found. Installing..."
    pip install numpy
fi

chmod +x pr12.py
chmod +x pr12_w.py

# Step 1: Create frames directory if it doesn't exist
mkdir -p frames

# Step 2: Extract frames from the video
ffmpeg -i bad_apple.mp4 frames/frame_%04d.png

# Step 3: Run the Python script to process the frames
./pr12.py 

# Step 4: Create processed_frames directory if it doesn't exist
mkdir -p processed_frames

# Step 5: Reassemble the frames into a video
ffmpeg -framerate 24 -i processed_frames/frame_%04d.png -c:v libx264 -pix_fmt yuv420p output_video.mp4

echo "Video processing complete."

./pr12_w.py

rm -r processed_frames frames

