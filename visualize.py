import sqlite3 # Importing the SQLite module.
import pandas as pd # Importing pandas for working with tabular data (DataFrames).
import seaborn as sns # Importing seaborn for advanced data visualization.
import matplotlib.pyplot as plt # Importing matplotlib’s plotting functions to customize and save plots.

def plot_price_vs_rating():  # Defining a function that generates a scatter plot of book price vs rating.
    df = pd.read_sql('SELECT price, rating FROM products', sqlite3.connect('products.db')) # Running an SQL query to fetch price and rating columns from the 'products' table, and to load the results directly into pandas DataFrame.
    sns.set(style='whitegrid') # Setting the visual style of seaborn plots to have a clean white grid background.
    plt.figure(figsize=(8,6)) # Creating a new figure for the plot with a specified size (8 inches wide, 6 inches tall).
    sns.scatterplot(data=df, x='price', y='rating') # Generating a scatter plot with price on the x-axis and rating on the y-axis.
    plt.title('Price vs Rating') # Adding a title to the plot.
    plt.savefig('static/plots/price_rating.png') # Saving the plot as a PNG image to the specified path.
    plt.close() # Closing the plot to free up memory and to avoid displaying it in non-interactive environments.

if __name__ == "__main__": # Runs the code only if this script is executed directly (not when imported as a module).
    plot_price_vs_rating() # Calls the function to generate and save the scatter plot.
    print("Chart saved.") # Prints a message to confirm that the chart has been successfully saved.
