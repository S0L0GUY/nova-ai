import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

def capture_vrchat_window():
    # Find the VRChat window
    window = gw.getWindowsWithTitle('VRChat')[0]  # Assuming the window title contains 'VRChat'
    
    # Get the position and size of the VRChat window
    left, top, width, height = window.left, window.top, window.width, window.height
    
    # Capture only the VRChat window area
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    frame = np.array(screenshot)
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

def detect_faces(frame):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt_tree.xml')
    
    # Convert the frame to grayscale (required by the classifier)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces

def main():
    while True:
        # Capture a frame from the VRChat window
        frame = capture_vrchat_window()
        
        # Detect faces in the frame
        faces = detect_faces(frame)
        
        # Draw rectangles around detected faces and print their coordinates
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            print(f"Detected face at coordinates: X={x}, Y={y}, Width={w}, Height={h}")
        
        # Show the frame with detected faces
        cv2.imshow('VRChat Face Detection', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
