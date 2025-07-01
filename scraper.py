# We're scraping the website -> "books.toscrape.com" (a site designed for practicing scraping).

import requests # Sends HTTP GET requests to load web pages.
from bs4 import BeautifulSoup # Parses the HTML and helps extract elements.
import db # A custom module (db.py) for storing data in a database (like SQLite).

BASE = "http://books.toscrape.com/catalogue/page-{}.html" # URL template. The {} will be replaced by the number of pages in website.

def scrape_all(): #Defining a function to scrape the data.
    data = [] #Empty list to store the scraped book data.
    for pg in range(1, 51): # Loops through pages 1 to 50.
        url = BASE.format(pg) #Format the URL for the current page number using BASE string.
        resp = requests.get(url) # Send a GET request to the page and gets the response.
        soup = BeautifulSoup(resp.text, 'html.parser') # Parse the HTML content using BeautifulSoup.
        for book in soup.select('article.product_pod'): # Select each book contained on the page.
            title = book.h3.a['title']  # Extract the book title from the 'title' attribute of the <a> tag.
            price = float(book.select_one('.price_color').text[1:]) # Extract the price and convert to float.
            rating = book.select_one('.star-rating')['class'][1] # Extract the star rating.
            link = 'http://books.toscrape.com/catalogue/' + book.h3.a['href'] # Build the full URL for the book detail page by appending the relative href to the base URL.
            availability = book.select_one('.instock.availability').text.strip()  # Extract availability info and strip whitespace/newlines.
            data.append((title, price, rating, availability, link)) # Append the extracted data as a tuple to the data list.
    return data # Returns the full list of scraped book data after looping through all the pages.

if __name__ == "__main__": # This ensures the code block only runs if the script is executed directly, not when imported as a module.
    db.create_table() # Call a method to create the database table, if it doesn't already exist. Presumably sets up the schema (columns like title, price, rating, etc).
    items = scrape_all() # Collects the list of book data (tuples of title, price, etc).
    db.insert(items)   # Insert the scraped book data into the database.
    print(f"Stored {len(items)} books.") # Prints a message showing how many books were successfully stored in the database.
