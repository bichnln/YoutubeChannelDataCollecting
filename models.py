from datetime import datetime

class Video:
    def __init__(self, vid, title, playlist, publishedDate):
        self.vid = vid
        self.title = title
        self.playlist = playlist
        self.publishedDate = datetime.strptime(
            publishedDate, "%Y-%m-%dT%H:%M:%SZ")
    
class Stats:
    def __init__(self, vid, recordedDate, viewCount, likeCount, dislikeCount, commentCount):
        self.vid = vid
        self.recordedDate = recordedDate
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.commentCount = commentCount
        

        
