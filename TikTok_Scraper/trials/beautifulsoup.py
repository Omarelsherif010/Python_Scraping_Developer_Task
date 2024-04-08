from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Function to search for a keyword on TikTok and return the page source
def search_tiktok_and_get_page_source(keyword):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Open TikTok website
        driver.get("https://www.tiktok.com/")

        # Wait for the page to load
        time.sleep(5)

        # Find the search bar element and enter the keyword
        search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/form/input')
        search_bar.send_keys(keyword)

        # Submit the search query
        search_bar.submit()

        # Wait for the search results to load
        time.sleep(5)

        # Return the page source
        return driver.page_source

    finally:
        # Close the webdriver
        driver.quit()

# Function to extract text and hashtag using Beautiful Soup
def extract_text_and_hashtag(page_source):
    # Create a Beautiful Soup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the element containing the text and hashtag
    div_element = soup.find('div', class_='css-f22ew5-DivMetaCaptionLine')

    # Extract text content from the element
    if div_element:
        span_text = div_element.find('span', class_='css-j2a19r-SpanText').get_text()
        hashtag = div_element.find('strong', class_='css-1p6dp51-StrongText').get_text()
        return span_text, hashtag
    else:
        return None, None

# Example usage
keyword = "pythonprogramming"
page_source = search_tiktok_and_get_page_source(keyword)
text, hashtag = extract_text_and_hashtag(page_source)
print("Text:", text)
print("Hashtag:", hashtag)
