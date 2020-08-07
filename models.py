from datetime import datetime
import requests
import json

class Video:
    def __init__(self, vid, title, playlist, publishedDate):
        self.vid = vid
        self.title = title
        self.playlist = playlist
        self.publishedDate = datetime.strptime(
            publishedDate, "%Y-%m-%dT%H:%M:%SZ")
    
class Stats:
    ''' Video statistics model '''
    def __init__(self, vid, recordedDate, viewCount, likeCount, dislikeCount, commentCount):
        self.vid = vid
        self.recordedDate = recordedDate
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.commentCount = commentCount


# get api_key and retrieve data from youtube API with entered api key
class YoutubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_channel_stats(self, channel_id):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={self.api_key}'
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data)
        try:
            data = data["items"][0]['statistics']
        except:
            data = None
        return data

    def get_playlist_title(self, playlist_id):
        url = f'https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={playlist_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        return data['items'][0]['snippet']['title']

    def get_playlist_items(self, playlist_id):
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId={playlist_id}&key={self.api_key}&maxResults=50'

        npt, result = self.get_playlist_items_per_page(url)
        # loop until there is no page left
        while (npt is not None):
            nexturl = url + "&pageToken=" + npt
            npt, next_result = self.get_playlist_items_per_page(nexturl)
            # add video retrieved to result one by one
            for i in next_result:
                result.append(i)
        return result

    def get_playlist_items_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        result = dict()

        # if this page does not return any playlist_items, return empty result and None as nextPageToken
        if 'items' not in data:
            return result, None

        result = data['items']
        nextPageToken = data.get('nextPageToken', None)
        return nextPageToken, result

    # for statistics
    def get_video_stats(self, video_id):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            # get only statistics of input video_id
            result = data['items'][0]['statistics']
        except:
            result = None
        return result

    def get_video_profile_by_id(self, video_id):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            result = data['items'][0]
        except:
            result = None
        return result
        

        
