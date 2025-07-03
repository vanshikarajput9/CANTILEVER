import requests # Importing the 'requests' library to enable sending HTTP requests.

url = "https://templatelab.com/wp-content/uploads/2017/08/business-report-template-28.jpg" # Image URL.

response = requests.get(url) # Sending a GET request to the image URL and storing the response in the 'response' variable.
with open("document.jpg", "wb") as f: # Opening a new file named 'document.jpg' in write-binary mode to save the image data.
    f.write(response.content) # Writing the image data to the file.

print("Image downloaded and saved as document.jpg") # Printing a confirmation message after the image is successfully downloaded and saved.


