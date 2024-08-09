import cv2
import numpy as np

def pixel_value_scaling(img):
    """Scales pixel values to the range [0, 1].

    Args:
        img: Input image.

    Returns:
        Scaled image.
    """
    min_val = np.min(img)
    max_val = np.max(img)
    scaled_img = (img - min_val) / (max_val - min_val)
    return scaled_img

def z_score_normalization(img):
    """Performs Z-score normalization on the image.

    Args:
        img: Input image.

    Returns:
        Normalized image.
    """
    mean = np.mean(img)
    std = np.std(img)
    normalized_img = (img - mean) / std
    return normalized_img


img = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

scaled_img = pixel_value_scaling(img)
normalized_img = z_score_normalization(img)

# Display or save the normalized images
cv2.imshow('Scaled Image', scaled_img)
cv2.imshow('Normalized Image', normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
