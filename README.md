# Youtube API Project
Uses the youtube data api to download thumbnails of youtubers.

# Setup Guide
- Clone the repo
# Getting the API Key
 - Go to https://console.developers.google.com
 - Sign in with your google account
 - Create a Project
 - Click on Add API's
 -Select "Youtube Data API v3"
 - Make credentials
 - Now , you have your API Key
 
# Some requirements
  - pip install libraries that are required ( pytube3 if u want to download the video)
  - Add your API key in the **api_key** variable as a string **api_key = "your_____api_____key"**
  - Make a list of youtubers along with their channel ids
  - **Note-** if you cannot find channel ids of certain channels <br> then go this website https://commentpicker.com/youtube-channel-id.php 
  
# Running it 
  - Run thumbnail_downloader.py
  - Enter the name of youtuber from the list
  - Then enter the channel id .
  - Let it run for few seconds
  - Voila!! You have a folder with the name of the youtuber you entered in which <br>the thumbnails of his recent videos are there are there
 
