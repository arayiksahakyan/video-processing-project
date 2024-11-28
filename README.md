# video-processing-project

Video Processing Project

This project automates video processing to extract frames, apply image processing (like background replacement and color modification), and reassemble the frames into a new video. The project is fully automated through a single Bash script.
Features

    Extract frames from an input video.
    Replace white objects in the frames with a new color (e.g., blue).
    Change the background of the frames with a custom background image.
    Reassemble the frames into a new video.
    Play the processed video.

Requirements

Before running the project, ensure that the following tools are installed:

    ffmpeg (for extracting frames and reassembling the video)
    Python 3.x (Python is used for processing the frames)
    OpenCV and NumPy libraries (these come bundled with the Python scripts)

You can install ffmpeg using the following commands:

# For Ubuntu/Debian
sudo apt-get install ffmpeg

# For macOS (using Homebrew)
brew install ffmpeg

Python libraries (OpenCV and NumPy) are already bundled with the Python scripts, so you don't need to install them manually.
Project Files

    pr12.sh: A Bash script that automates the entire video processing workflow:
        Checks if the necessary files exist (input video and Python scripts).
        Extracts frames from the input video using ffmpeg.
        Processes the frames by replacing white objects and changing the background.
        Reassembles the frames into a new video using ffmpeg.

    pr12.py: A Python script that processes the extracted frames:
        Loads a background image.
        Replaces white objects with a new color.
        Changes the background of the frames.
        Saves the processed frames.

    pr12_w.py: A Python script that plays the processed video (output_video.mp4).

    pexels-padrinan-255379.jpg: The background image used for replacing the original background.

    bad_apple.mp4: The input video file. You can replace this with your own video.

Usage

    Clone the repository to your local machine:

git clone https://github.com/your-username/video-processing-project.git
cd video-processing-project

Place your input video (e.g., bad_apple.mp4) and the background image (e.g., pexels-padrinan-255379.jpg) in the project directory.

Run the Bash script to process the video:

./pr12.sh

The pr12.sh script will automatically:

    Extract frames from the input video.
    Process the frames by replacing white objects and changing the background.
    Reassemble the frames into a new video (output_video.mp4).

The processed video will be saved as output_video.mp4.

Optionally, play the processed video using:

    python3 pr12_w.py

Contributing

Feel free to fork this repository and submit pull requests. If you have any improvements or bug fixes, feel free to contribute!

