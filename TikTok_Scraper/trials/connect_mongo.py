from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pymongo import MongoClient

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tiktok_db"]
    collection = db["tiktok_data_1"]
    return collection

# Function to search inside TikTok using Selenium
def search_tiktok_and_save_to_mongodb(keyword):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Open TikTok website
        driver.get("https://www.tiktok.com/")

        # Wait for the page to load
        time.sleep(10)

        # Find the search bar element
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')

        # Enter the search query (keyword) into the search bar
        search_bar.send_keys(keyword)

        # Submit the search query (press Enter)
        search_bar.submit()

        # Wait for the search results to load
        time.sleep(10)

        # Extract and process the search results
        search_results = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/a')
        for result in search_results:
            title = result.get_attribute("title")
            video_link = result.get_attribute("href")

            # Check if the data already exists in MongoDB
            if not collection.find_one({"title": title, "video_link": video_link}):
                # If the data does not exist, scrape it and save it to MongoDB
                data = {
                    "title": title,
                    "video_link": video_link,
                    "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                collection.insert_one(data)
                print(f"Data saved to MongoDB: {data}")

    finally:
        # Close the webdriver
        driver.quit()
 
# Connect to MongoDB
collection = connect_to_mongodb()

# Example usage: Search for videos related to "pythonprogramming" on TikTok
search_tiktok_and_save_to_mongodb("pythonprogramming")
