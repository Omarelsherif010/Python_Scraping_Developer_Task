import requests
import json
import os

# Function to scrape TikTok videos and save them into files
def scrape_tiktok_videos(username, num_videos=3):
    # Make a request to TikTok's API to get videos
    api_url = f"https://www.tiktok.com/node/share/user/@{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    params = {"count": num_videos, "id": username}
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Create a directory to save the videos
        os.makedirs(username, exist_ok=True)
        
        # Loop through the videos and save them into files
        for video_data in data["body"]["itemListData"]:
            video_url = video_data["itemInfos"]["video"]["urls"][0]
            video_id = video_data["itemInfos"]["id"]
            file_path = os.path.join(username, f"{video_id}.mp4")
            
            # Download the video and save it into a file
            with open(file_path, "wb") as f:
                f.write(requests.get(video_url).content)
            
            print(f"Saved video {video_id} as {file_path}")
    else:
        print(f"Failed to fetch videos. Status code: {response.status_code}")

# Example usage: Scrape 5 videos from a TikTok user named "example_user"
scrape_tiktok_videos("dailysabry", num_videos=5)
