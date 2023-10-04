# Import libraries
import logging
import psycopg2
import configparser
from psycopg2 import sql
import json

# Import configuration to connect to database (PostgreSQL)
parser = configparser.ConfigParser()
parser.read("keys.conf")
hostname = parser.get("pg_config", "hostname")
dbname = parser.get("pg_config", "dbname")
user = parser.get("pg_config", "user")
password = parser.get("pg_config", "password")

# Function to define new database
def defineDB(db_name):
    logging.info(f"Creating database {db_name}.")
    try:
        conn = psycopg2.connect(f"host = {hostname} dbname={dbname} user = {user} password = {password}")
        cursor = conn.cursor()
        conn.autocommit = True
        query = f"CREATE DATABASE {db_name};"
        cursor.execute(query)
        cursor.close()
        logging.info("Database created successfully.")
    except psycopg2.Error as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()

# Create connection to given database
def create_connection(db_name):
    logging.info(f"Connecting to database {db_name}.")
    conn = psycopg2.connect(f"host = {hostname} dbname = {db_name} user = {user} password = {password}")
    conn.autocommit = True
    return conn

# Load the data to a database
def load_data(data_path, conn):
    
    # Set the correct encoding
    conn.set_client_encoding('UTF8')

    # Create cursor
    logging.info("Creating cursor.")
    try:
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print(e)
    
    # Create table for the data
    logging.info("Creating table to store the data.")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS rtable(id SERIAL PRIMARY KEY, author VARCHAR, date TIMESTAMP, num_comments INT, upvotes INT);")
    except psycopg2.Error as e:
        print(e)
    
    # Insert data in the table
    logging.info("Loading data in the table.")
    with open(data_path, encoding="utf-8-sig") as data_file:
        data = json.load(data_file)
    # Define query to insert data
    insert_query = """INSERT INTO rtable (id, author, date, num_comments, upvotes) 
                    VALUES (%s, %s, %s, %s, %s)"""
    for k,v in data.items():
        cursor.execute(insert_query, (int(k.split("_")[1]), v['author'], v['datetime'], int(v['num_comments']), int(v['upvotes'])))
    
    #  Close connection
    cursor.close()
    conn.close()
    logging.info("Data loaded successfully. Closing connection.")
