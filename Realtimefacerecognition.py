import cv2
import numpy as np

def process_frame(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Scale pixel values
    scaled_frame = gray_frame / 255.0
    
    # Standardize pixel values
    mean = np.mean(gray_frame)
    std_dev = np.std(gray_frame)
    standardized_frame = (gray_frame - mean) / std_dev
    
    return scaled_frame, standardized_frame

# In a video stream processing loop
cap = cv2.VideoCapture(0)  # Capture from the webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    scaled_frame, standardized_frame = process_frame(frame)
    
    # Display the processed frames (for visualization or further processing)
    cv2.imshow('Scaled Frame', scaled_frame)
    cv2.imshow('Standardized Frame', standardized_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
