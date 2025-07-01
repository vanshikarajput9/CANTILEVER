from flask import Flask, request, render_template # Helps import Flask to create the web app, request to access query parameters, render_template to render HTML templates.
import sqlite3 # Imports sqlite3 to connect.
import visualize # Imports your visualize module to generate the price vs rating chart.

app = Flask(__name__) # Creates a Flask web app instance.

@app.route('/', methods=['GET']) # Defines a route for the home page ("/"), which only allows GET requests.
def index(): 
    term = request.args.get('q', '')  # Gets the search term from the URL query string. Default is an empty string if nothing is provided.
    conn = sqlite3.connect('products.db')  # Connects to the SQLite database.
    cur = conn.cursor() # Creates a cursor object to execute SQL queries.
    if term:
        cur.execute("SELECT title, price, rating, description FROM products WHERE title LIKE ?", (f'%{term}%',)) # If a search term is given, fetch products whose titles contain the term (case-insensitive).
    else:
        cur.execute("SELECT title, price, rating, description FROM products") # If no search term, fetch all products.
    products = cur.fetchall()  # Retrieves all matching rows as a list of tuples.
    conn.close() # Closes the database connection to avoid leaks.
    visualize.plot_price_vs_rating() # Calls the visualization function to generate the latest plot image. This ensures the chart is always up to date with the current database.
    return render_template('index.html', products=products, query=term) # Renders the HTML template, passing the product list and search query to it.

if __name__ == "__main__": # Run this block only if the script is executed directly (not when imported)
    app.run(debug=True) # Start the Flask development server with debugging enabled.
 
