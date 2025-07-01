import sqlite3 # Imports the built-in module to interact with SQLite databases.

DB = 'products.db' # Defines the name of the SQLite database file. If it doesn't exist, it will be created.

def create_table():  # Creates the 'products' table if it doesn't already exist.
    with sqlite3.connect(DB) as conn: # Opens a connection to the database file."with" ensures the connection is properly closed after the block executes.
        conn.execute(''' 
          CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,
            rating REAL,
            description TEXT
          )''')
          # Execute a SQL command to create a table named 'products' with 5 columns:
          # 1 - id: primary key (auto-incremented)
          # 2 - title: text (book title)
          # 3 - price: real number (float)
          # 4 - rating: real number (converted from star rating text)
          # 5 - description: text (e.g., availability or any additional info)
          # The table will only be created if it doesn't already exist.

def insert_products(items): # Function for inserting multiple product records into the 'products' table.
    with sqlite3.connect(DB) as conn: # Opens a connection to the database.
        conn.executemany(
          'INSERT INTO products (title, price, rating, description) VALUES (?, ?, ?, ?)',
          items
        )
        # Use executemany() to insert the list of product tuples (title, price, rating, description).
        # Each "?" placeholder is replaced with the values from each tuple in the 'items' list.
