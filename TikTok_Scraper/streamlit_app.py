import streamlit as st
from tiktok_scraper import TikTokScraper

def main():
    st.title("TikTok Scraper")

    # User input for database and collection or use default values
    db_name = st.text_input("Enter database name", value="tiktok_db")
    collection_name = st.text_input("Enter collection name", value="tiktok_data")

    # Initialize TikTokScraper object
    tiktok_scraper = TikTokScraper(db_name=db_name, collection_name=collection_name)

    # User chooses scraping option
    option = st.radio("Choose scraping option", ("Search by Keyword", "Scrape TikTok Profile"))

    if option == "Search by Keyword":
        # User input for keyword
        keyword = st.text_input("Enter keyword to search on TikTok")

        # Button to trigger scraping and saving to MongoDB
        if st.button("Search and Save to MongoDB"):
            st.info("Scraping TikTok and saving data to MongoDB...")
            tiktok_scraper.search_and_save_to_mongodb(keyword)
            st.success("Data saved successfully!")

    elif option == "Scrape TikTok Profile":
        # User input for TikTok username
        username = st.text_input("Enter TikTok username")

        # Button to trigger scraping TikTok profile and saving to MongoDB
        if st.button("Scrape TikTok Profile"):
            st.info("Scraping TikTok profile and saving data to MongoDB...")
            tiktok_scraper.scrape_tiktok_profile(username)
            st.success("Profile data saved successfully!")

if __name__ == "__main__":
    main()
