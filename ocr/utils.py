import cv2
import numpy as np
from PIL import Image
import pytesseract

# Tesseract setup
pytesseract.pytesseract.tesseract_cmd = r"your_path\tesseract.exe"

def preprocess_image(image: Image.Image) -> np.ndarray:
    """Convert to grayscale and threshold for better OCR accuracy."""
    img = np.array(image.convert("L"))
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    return img

def extract_text(image: np.ndarray) -> str:
    """Run OCR on preprocessed image."""
    return pytesseract.image_to_string(image)
