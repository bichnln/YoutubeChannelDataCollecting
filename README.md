# YoutubeChannelScraping
This is a small tool used for scraping a channel's statistic data (view count, subscriber count, and number of published videos) and its video's data (view count, like count, dislike count, and comment count).

1. The tool is designed and written based on how the author's target channel organises its content. 

2. Collected data is stored in local MongoDB database, so make you need to have MongoDB installed on your machine. 

3. There are two essential json files: the first one (youtube_credentials.json) stores Youtube API Key and the second one (dreamcatcher_ids.json) stores the target channel's id and its playlists' id. 
  3.1. Replace '<add your own api key here>' with your own Youtube API key in youtube_credentials.json
  3.2. Replace the values of "channel_id" and "id" in "playlists" array to collect data of other channel and its videos. Make sure to follow the current structure of the current json file.

4. There are 2 scripts that can be executed: 
  4.1. main.py - this script read the json files, sends requests to Youtube API to get data of the channel and playlists whose id are written in the second json file, and stores data to local MongoDB database.
  4.2. retrieveData.py is used for retrieving data stored in the database and exporting data to a csv file. 

