Image Normalization for Real-Time Face Recognition

This project implements image normalization techniques for real-time face recognition using OpenCV (cv2) and NumPy libraries.

Description

Normalizing image pixel values is a crucial pre-processing step in image processing tasks, including face recognition. It helps to improve the performance and accuracy of algorithms by ensuring data is on a common scale. This project demonstrates two common normalization techniques:

Scaling: Scales pixel values between a desired range, typically 0 and 1.
Standardization: Subtracts the mean and divides by the standard deviation, centering the data around zero with a unit standard deviation.
Benefits of normalization:

Reduces the influence of illumination variations.
Improves the effectiveness of distance metrics used for comparison.
Enables better convergence during model training (if applicable).

Features

1. Real-time image acquisition from webcam.
2. Image conversion to grayscale.
3. Scaling pixel values to the range [0, 1].
4. Standardization of pixel values with zero mean and unit standard deviation.

Installation

Ensure you have Python 3 and OpenCV (cv2) installed. You can install OpenCV using pip install opencv-python.

Usage

Run the script using python Realtimefacerecognition.py

The script will display two windows:

Scaled Frame: Shows the image with pixel values scaled to [0, 1].

Standardized Frame: Shows the image with pixel values centered and normalized.

Press 'q' on your keyboard to exit the program.

