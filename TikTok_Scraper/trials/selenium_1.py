from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scroll_to_load_videos(driver):
    # Scroll down to load more videos
    for _ in range(5):  # Adjust the number of scrolls as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for more videos to load

def scrape_tiktok_profile(username):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Open TikTok profile page
        driver.get(f"https://www.tiktok.com/@{username}")
        time.sleep(20)  # Wait for page to load
        
        # Click on "Continue as guest" if it exists
        try:
            continue_as_guest_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/div')
            continue_as_guest_btn.click()
            time.sleep(5)  # Wait for the page to reload after clicking
        except:
            pass

        # Find elements by XPath to extract profile information
        following = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[1]/strong').text
        followers = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong').text
        likes = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[3]/strong').text
        
        # Print profile information
        print("Following:", following)
        print("Followers:", followers)
        print("Likes:", likes)
        
        # Scroll to load more videos
        scroll_to_load_videos(driver)
        
        # Find video elements
        video_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/a')
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

# Example usage: Scrape TikTok profile information for a user named "dailysabry"
scrape_tiktok_profile("dailysabry")
