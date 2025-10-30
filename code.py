import cv2
import os
import time
import numpy as np

VIDEO_PATH = r"C:\Users\hp\OneDrive\Desktop\spidermanCode\spiderman.mp4"

# ⬇️ Reversed so letters form the main object
ASCII_CHARS = " .!:-=+*#%@"

def frame_to_ascii(frame, width=120, height=40):
    frame = cv2.resize(frame, (width, height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ascii_frame = ""
    for y in range(height):
        for x in range(width):
            brightness = gray[y, x]
            char_index = int(brightness / 255 * (len(ASCII_CHARS) - 1))
            ascii_frame += ASCII_CHARS[char_index]
        ascii_frame += "\n"
    return ascii_frame

def play_video_ascii(video_path, width=120, height=40):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Cannot open video. Check file path.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = 1 / fps if fps > 0 else 0.04

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = frame_to_ascii(frame, width, height)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)
            time.sleep(delay * 0.9)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("Playback ended.")

if __name__ == "__main__":
    play_video_ascii(VIDEO_PATH, width=280, height=65)
