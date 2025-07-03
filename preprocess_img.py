# Make sure Tesseract OCR is installed on your system.

import cv2 # Import the OpenCV library for image processing.

# Load image into the variable.
image = cv2.imread('document.jpg')

# Convert to grayscale (removing color to simply processing).
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optional: Apply thresholding to enhance text visibility.
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Save processed image.
cv2.imwrite('processed.jpg', thresh)

print("Image processed and saved as processed.jpg") # Print a confirmation message after saving the processed image.
