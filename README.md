### TikTok Scraper (Working)
You will find three important files inside TitkTok_Scraper(Working):
1. [tiktok_scraper.py](TikTok_Scraper\tiktok_scraper.py) -> contains a class called TikTokScraper which includes all the functions needed.
2. [streamlit_app.py](TikTok_Scraper\streamlit_app.py) -> contains easy to use interface to play around the scraping functions
3. [requirements.txt](TikTok_Scraper\requirements.txt) -> contains all the required packages to run the code (Main packages are selenium, pymongo, beautifulsoup, streamlit)

To run the code on you device, you need to do the following steps:
1. create virtual environment to install our libraries inside through this command `python -m venv venv`
2. activate the venv through `source venv/Scripts/activate` (this command is for bash)
3. install all required libraries from requirements.txt file by running this command `pip install -r requirements.txt`
4. you can run the code in two ways:
   <ol>
   <li>  run tiktok_scraper.py directly after you enter (keyword or username) in main function at the end of the file </li>
    <li> run streamlit_app.py to have nice interface in which you can enter (keyword, username, db_name, collection)
        , you can do this through this command `streamlit run streamlit_app.py` (make sure you are inside TitkTok_Scraper directory) </li>
   </ol>
6. fill the required fields and let the magic happen
7. check your MongoDB collection and congratulation

----
Functions inside TikTokScraper class in tiktok_scraper.py file:
1. __int__() -> to intailize the database connection and choose or create collection
2. scroll_to_load_videos() -> to give you the ability to scroll in order to load more videos
3. search_and_save_to_mongodb(keyword) -> function that uses selenium to search on tiktok using the keyword entered as follows:
                                            <ol>
                                            <li> use XPATH to find search bar and write the keyword</li>
                                            <li> wait for page to load then use scroll_to_load_videos() to load more videos</li>
                                            <li> use XPATH to scrape video_links, upload_dates, and captions</li>
                                            <li> enumerate through video_results and use beautifulsoup to extract text and hashtags from captions</li>
                                            <li> check if video link existes in database collection then insert it to mongoDB using pymongo</li>
                                            <li> we have another collection to track the duplicated scraped data</li>
                                            </ol>
4. scrape_tiktok_profile(username) -> function that uses selenium to scrape data from specific profile using username:
                                        <ol>
                                        <li>search the profile using username</li>
                                        <li>scrape profile info like following, followers, likes</li>
                                        <li>scroll_to_load_videos</li>
                                        <li>scrape videos info</li>
                                        <li>extract title and video link then check if it is not in database collection and insert it using pymongo</li>
                                        <li>we also have another collection for duplicated scraped data</li>
                                        </ol>
<be>

-----
<br>
streamlit_app.py in details:

1. User Input: Input database and collection names.
2. Scraping Options: Choose between keyword search or profile scraping.
3. Scraping by Keyword: Input keyword and initiate scraping.
4. Scraping TikTok Profile: Input username and start scraping.

<br>

-----

<br>

> Note: You need to click `continue as guest` in TikTok when starting the scraping script as this part of the code don't work properly
<br>

-----
<be>

### Twitter Scraper (Not Working)

1. Twitter has blocked public to their data and we need to create account on Twitter Developer to use their API.
2. Famous tools like snscrape, tweepy, twscrape are not working anymore without creating app at twitter developer.
3. The free version of twitter api don't allow read data, just allow writing few number of tweets

Here are some links to read more about the current situation of scraping twitter data:

1. https://github.com/JustAnotherArchivist/snscrape/issues/996 (twitter added a login wall that blocks scraping data without using their official API)
2. https://developer.twitter.com/en (Different Twitter API plans and prices)
3. https://increditools.com/twitter-scrapers/ (ready to use tools to scrape twitter - not free)



                                            


