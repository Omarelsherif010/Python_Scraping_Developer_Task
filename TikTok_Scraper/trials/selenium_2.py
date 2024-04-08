from selenium import webdriver
from selenium.webdriver.common.by import By
import time

### Notes
# 1. when using keyword to search, the href and caption are not on the same xpath so I need to handle this while collecting information

def search_tiktok(keyword):
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
        print('Done')
        # Wait for the search results to load
        time.sleep(10)

        # Optionally, you can scroll down to load more search results
        # Example:
        # for _ in range(5):  # Adjust the number of scrolls as needed
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2)  # Wait for more search results to load

        # Extract and process the search results as needed
        # Example: Print the titles of the search results
        # Find video elements
        video_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/a')
        print(f'Number of videos: {len(video_elements)}')
        
        # Extract title and link of each video uploaded after 2022
        for i, video_element in enumerate(video_elements, 1):
            video_title = video_element.get_attribute("title")
            video_link = video_element.get_attribute("href")
            print(f"Video {i}:")
            print("Title:", video_title)
            print("Link:", video_link)

    finally:
        # Close the webdriver
        driver.quit()

# Example usage: Search for videos related to "pythonprogramming" on TikTok
search_tiktok("pythonprogramming")
