# Simple Reddit Data ETL Pipeline

## Introduction
This is a basic ETL (Extract, Transform, Load) pipeline for Reddit data. The pipeline scrapes data from the League of Legends subreddit, specifically the top posts of the day, and loads it into a PostgreSQL database. This project focuses on the extraction and loading steps, omitting the transformation phase. It uses `psycopg2` for PostgreSQL interaction and stores database credentials in a `keys.conf` configuration file.

## Prerequisites
Before running the ETL pipeline, ensure you have the following prerequisites:

1. Python 3.x installed.
2. PostgreSQL server installed and running.
3. Install the `psycopg2` library using pip: `pip install psycopg2`.
4. Install the `configparser` library using pip: `pip install configparser`
5. Create a `keys.conf` configuration file with PostgreSQL credentials in the following format:

    ```plaintext
    [pg_config]
    hostname = localhost
    dbname = postgres
    user = postgres
    password = your_password
    ```

## Usage
1. Clone this repository to your local machine.
2. Create the `keys.conf` file with your PostgreSQL credentials (as described above) and save it in the project directory.
3. Execute the ETL pipeline script using the following command:

    ```bash
    python etl_pipeline.py
    ```

   This will run the pipeline, scraping Reddit data and loading it into the database.

## Brief Code Description
The `etl_pipeline.py` script performs the following tasks:

### 1. Data Extraction
   - Scrapes data from Reddit's League of Legends subreddit.
   - Extracts information such as title, author, posting date/time, number of comments, and upvotes.
   - Stores the extracted data in a JSON file.

### 2. Database Connection and Creation
   - Reads PostgreSQL credentials from `keys.conf`.
   - Connects to the PostgreSQL server.

### 3. Database Setup
   - Checks if the `redditdb` database exists; if not, it creates the database.
   - Defines the table structure with appropriate data types to store the Reddit data.

### 4. Data Loading
   - Connects to the `redditdb` database.
   - Creates a table in the database to store Reddit data.
   - Loads the extracted data from the JSON file into the database table.

## Note
This is a basic project intended for educational purposes. Depending on your requirements, you may want to implement error handling, logging, and additional data validation or transformation steps to make the pipeline more robust and suitable for production use.
