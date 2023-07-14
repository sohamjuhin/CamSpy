# CamSpy
webcam key logger
##This code will take a screenshot of the entire screen and a picture from the webcam, and save them to files with the current time and date as the filenames. To run the code, you will need to have the pyautogui and cv2 modules installed.
##You can install them by running the following commands in the terminal:


pip install pyautogui

pip install opencv-python

##Once the modules are installed, you can run the code by saving it as a .py file and then running it from the terminal. For example,
##if you saved the code as keylogger.py, you would run it by running the following command:

python keylogger.py

The screenshots and pictures will be saved in the current directory. You can open them by double-clicking on them.

Here is an explanation of the code:

The import pyautogui and import cv2 lines import the pyautogui and cv2 modules.
The take_screenshot() function takes a screenshot of the entire screen and saves it to a file.
The take_webcam_picture() function takes a picture from the webcam and saves it to a file.
The if __name__ == "__main__": block is the main execution block of the code. It calls the take_screenshot() and take_webcam_picture() functions.
