import streamlit as st
from tiktok_scraper import TikTokScraper

def main():
    st.title("TikTok Scraper")

    # User input for keyword and database/collection names
    keyword = st.text_input("Enter keyword to search on TikTok")
    db_name = st.text_input("Enter database name", value="tiktok_db")
    collection_name = st.text_input("Enter collection name", value="tiktok_data")

    # Initialize TikTokScraper object
    tiktok_scraper = TikTokScraper(db_name=db_name, collection_name=collection_name)

    # Button to trigger scraping and saving to MongoDB
    if st.button("Search and Save to MongoDB"):
        st.info("Scraping TikTok and saving data to MongoDB...")
        tiktok_scraper.search_and_save_to_mongodb(keyword)
        st.success("Data saved successfully!")

    # Button to trigger scraping TikTok profile and saving to MongoDB
    if st.button("Scrape TikTok Profile"):
        username = st.text_input("Enter TikTok username")
        st.info("Scraping TikTok profile and saving data to MongoDB...")
        tiktok_scraper.scrape_tiktok_profile(username)
        st.success("Profile data saved successfully!")

if __name__ == "__main__":
    main()
