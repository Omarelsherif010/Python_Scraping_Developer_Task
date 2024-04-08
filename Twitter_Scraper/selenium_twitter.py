# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Path to your webdriver executable (e.g., chromedriver)
# # webdriver_path = "H:\\2024 - Programs\chrome-win64\chrome-win64\chrome.exe"

# # Initialize the webdriver (assuming Chrome)
# driver = webdriver.Chrome()

# # Open Twitter sign-in page in the browser
# driver.get("https://twitter.com/login")

# # Wait for the sign-in page to load
# time.sleep(2)

# # Find the username and password input fields and enter your credentials
# username_input = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
# username_input.send_keys("omarelsherif010@gmail.com")
# password_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
# password_input.send_keys("Collegeboard@010#twitter")
# password_input.send_keys(Keys.RETURN)

# # Wait for the sign-in process to complete
# time.sleep(5)  # Adjust as needed

# # Open Twitter search page in the browser
# driver.get("https://twitter.com/search?q=python%20programming")

# # Wait for the page to load
# time.sleep(2)

# # Scroll down to load more tweets (repeat as needed)
# for _ in range(5):  # Adjust the number of scrolls as needed
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)

# # Find and extract tweet elements
# tweet_elements = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

# # Extract tweet text
# tweets = [tweet.text for tweet in tweet_elements]

# # Print the scraped tweets
# for tweet in tweets:
#     print(tweet)

# # Close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Uncomment this line if you want to run in headless mode
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

# Initialize the webdriver with configured options
driver = webdriver.Chrome(options=chrome_options)

# Open Twitter profile page in the browser
driver.get("https://twitter.com/omarelsherif010")

# Wait for the page to load
time.sleep(5)  # Adjust as needed

# Capture a screenshot of the profile page
driver.save_screenshot("twitter_profile.png")

# Close the browser
driver.quit()
