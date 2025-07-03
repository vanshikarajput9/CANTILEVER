import pytesseract  # import the pytesseract library for OCR.
from PIL import Image # Import the Image class from the Pillow library for opening and handling image files.

# Optional: Point to tesseract executable if needed.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load processed image.
img = Image.open("processed.jpg")

# Extract text.
extracted_text = pytesseract.image_to_string(img)

# Save to file or print.
with open("extracted_text.txt", "w") as f:
    f.write(extracted_text)

print("Text extracted and saved to extracted_text.txt")
