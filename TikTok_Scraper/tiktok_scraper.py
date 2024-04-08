from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from pymongo import MongoClient

class TikTokScraper:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["tiktok_db"]
        self.collection = self.db["tiktok_data"]
        self.duplicate = self.db["tiktok_data_duplicate"]
        self.driver = webdriver.Chrome()

    def scroll_to_load_videos(self):
        # Scroll down to load more videos
        for _ in range(5):  # Adjust the number of scrolls as needed
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for more videos to load

    def search_and_save_to_mongodb(self, keyword):
        try:
            # Open TikTok website
            self.driver.get("https://www.tiktok.com/")

            # Wait for the page to load
            time.sleep(10)

            # Find the search bar element
            search_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')

            # Enter the search query (keyword) into the search bar
            search_bar.send_keys(keyword)

            # Submit the search query (press Enter)
            search_bar.submit()

            # Wait for the search results to load
            time.sleep(20)

            # Extract and process the search results
            search_results = self.driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/a')
            

            time.sleep(20)

            for i, result in enumerate(search_results, start=0):
                # title = title_value.get_attribute("title")
                video_link = result.get_attribute("href")

                upload_dates = self.driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/a/div/div[2]/div')
                print(upload_dates)
                upload_date = upload_dates[i].text
                print(upload_date)
                
                caption = self.driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]')
        
                title_hashtags = caption[i].get_attribute('outerHTML')
                soup = BeautifulSoup(title_hashtags, 'html.parser')
                
                # Extract text content
                text_content = soup.text

                # Extract hashtags
                hashtags = [tag.text for tag in soup.find_all('strong')]
                
                # Check if the data already exists in MongoDB
                if not self.collection.find_one({"video_link": video_link}):
                    # If the data does not exist, scrape it and save it to MongoDB
                    data = {
                        "video_link": video_link,
                        "upload_date": upload_date,
                        "text_content": text_content,
                        "hashtags": hashtags,
                        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.collection.insert_one(data)
                    print(f"Data saved to MongoDB: {data}")
                
                elif not self.collection.find_one({"video_link": video_link}):

                    data = {
                        "video_link": video_link,
                        "upload_date": upload_date,
                        "text_content": text_content,
                        "hashtags": hashtags,
                        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.duplicate.insert_one(data)
                    print(f"Deplicated Data saved to MongoDB: {data}")

        finally:
            # Close the webdriver
            # self.driver.quit()
            print('search and save to mongodb done correctly')

    def scrape_tiktok_profile(self, username):
        try:
            # Open TikTok profile page
            self.driver.get(f"https://www.tiktok.com/@{username}")
            time.sleep(20)  # Wait for page to load
            
            # # Click on "Continue as guest" if it exists
            # try:
            #     continue_as_guest_btn = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/div')
            #     continue_as_guest_btn.click()
            #     time.sleep(5)  # Wait for the page to reload after clicking
            # except:
            #     pass

            # Find elements by XPath to extract profile information
            following = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[1]/strong').text
            followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[2]/strong').text
            likes = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/h3/div[3]/strong').text
            
            # Print profile information
            print("Following:", following)
            print("Followers:", followers)
            print("Likes:", likes)
            
            # Scroll to load more videos
            self.scroll_to_load_videos()
            
            # Find video elements
            video_elements = self.driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/a')
            print(f'Number of videos: {len(video_elements)}')
            
            # Extract title and link of each video
            for i, video_element in enumerate(video_elements, 1):
                video_title = video_element.get_attribute("title")
                video_link = video_element.get_attribute("href")
                
                if not self.collection.find_one({"video_link": video_link}):
                    # If the data does not exist, scrape it and save it to MongoDB
                    data = {
                        "title": video_title,
                        "video_link": video_link,
                        "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    self.collection.insert_one(data)
                    print(f"Profile Data saved to MongoDB: {data}")
                
        finally:
            # Close the webdriver
            # self.driver.quit()
            print('Get videos from profile and save to mongodb done correclty')

# Example usage
def main():
    tiktok_scraper = TikTokScraper()
    tiktok_scraper.search_and_save_to_mongodb("english")
    # tiktok_scraper.scrape_tiktok_profile("dailysabry")

if __name__ == "__main__":
    main()