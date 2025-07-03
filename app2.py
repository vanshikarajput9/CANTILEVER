from flask import Flask, request, render_template, redirect, url_for # Import necessary modules from Flask and other libraries.
import pytesseract # For OCR (extracting text from images).
from PIL import Image # For image handling.
import os # For file and path operations.

app = Flask(__name__) # Create a Flask app instance.
UPLOAD_FOLDER = 'uploads' # Define a folder to store uploaded images.
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Create the folder if it doesn't exist.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Add upload folder path to app config.

@app.route('/', methods=['GET', 'POST']) # Define the main route ('/') that handles both GET and POST requests.
def upload_image(): 
    if request.method == 'POST': # If form was submitted via POST method.
        file = request.files['image']  # Get the uploaded file from the form.
        if file: # Check if a file was actually uploaded.
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)  # Build the file path where the image will be saved.
            file.save(filepath)  # Save the uploaded image to the server.

            # OCR
            text = pytesseract.image_to_string(Image.open(filepath))
            return render_template('result.html', text=text) # Render the result template and pass the extracted text to it.
    return render_template('index.html') # If request is GET, render the upload form.

# Start the Flask development server.
if __name__ == '__main__':
    app.run(debug=True) 
