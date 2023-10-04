# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import logging

def scrap_data(url):
    
    # Log
    logging.info("Initializing scrapping process.")

    # Set driver
    driver = webdriver.Chrome(executable_path='C:/Users/adars/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver.get(url)

    # Get the div element (for post content and votes)
    div_elements = driver.find_elements(By.CLASS_NAME, "top-matter")
    divs_likes = driver.find_elements(By.CLASS_NAME, "midcol.unvoted")

    # Dict to store the data
    data_scrapped = {}

    # iterate through the divs detected previously
    for i, (div, div_likes) in enumerate(zip(div_elements, divs_likes)):
        try:
            # get the relevant info
            title = div.find_element(By.CLASS_NAME, "title").find_element(By.CLASS_NAME, "title").text
            p_element = div.find_element(By.CLASS_NAME, "tagline")
            author = p_element.find_element(By.CLASS_NAME, "author.may-blank").text
            date_time = p_element.find_element(By.CSS_SELECTOR, 'time').get_attribute('datetime')
            num_comments = div.find_element(By.CLASS_NAME, "flat-list.buttons").find_element(By.CLASS_NAME, "first").text.split(" ")[0]
            likes = div_likes.find_element(By.CLASS_NAME, "score.unvoted").text

            # Save each post data
            data_scrapped[f'post_{i}'] = {
                'title': title,
                'author': author,
                'datetime': date_time,
                "num_comments": num_comments,
                "upvotes": likes
            }
        except:
            # We ignore the advertisement posts (they give error since they don't contain datetime element)
            pass
    
    # Define JSON file and store the data
    json_filename = "reddit_data.json"
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(data_scrapped, json_file, ensure_ascii=False, indent=4)
    
    logging.info(f"Scrapped data saved to {json_filename} successfully.")
    return json_filename
