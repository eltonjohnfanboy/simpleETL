from data_scrapping import scrap_data
from utils import init_logger
from data_loading import load_data, create_connection, defineDB
import logging

if __name__ == '__main__':

    # Initialize the logger
    init_logger()

    # Scrape the data
    url = "https://old.reddit.com/r/leagueoflegends/top/"
    data_path = scrap_data(url)

    # Define the database
    db_name = 'redditdb'
    defineDB(db_name)

    # Create connection and load data in the database created previously
    conn = create_connection(db_name)
    logging.info(f"Connected successfully to {db_name}.")
    load_data(data_path, conn)