import json
import requests
from datetime import date, datetime
from pymongo import MongoClient
import csv


def retrieveChannelStats(outputFile: str):
    subscriberCounts = []
    dates = []
    for item in channel.find({}):
        try: 
            print(f'Channel subscriber count: {item.get("subscriberCount")} on date {item.get("recorded_date").date()}')
            subscriberCounts.append(item.get('subscriberCount'))
            dates.append(item.get('recorded_date').date())
        except:
            print('Errors retrieving channel stats.')
    
    outputFile = outputFile + '.csv'

    try: 
        with open(outputFile, 'w', newline='') as file:
            fieldnames = ['Date', 'Subscriber Count']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0, len(subscriberCounts)):
                writer.writerow({'Date': dates[i], 'Subscriber Count': subscriberCounts[i]})
    except:
        print('Errors writing to file')

def retrieveVideoStats(vid: str, outputFile: str):
    ''' Take video's id and name of the file to which the result would be exported  '''
    dates = []
    viewCounts = []
    likeCounts = []
    commentCounts = []

    for item in statisticsCollection.find({"vid": vid}):
        try: 
            dates.append(item.get('recorded_date').date())
            viewCounts.append(item.get('viewCount'))
            likeCounts.append(item.get('likeCount'))
            commentCounts.append(item.get('commentCount'))
        except: 
            print('Errors getting stats attributes')
        
    outputFile = outputFile + '.csv'

    try: 
        with open(outputFile, 'w', newline='') as file:
            fieldnames = ['Date', 'View Count', 'Like Count', 'Comment Count']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0, len(dates)):
                writer.writerow({'Date': dates[i], 'View Count': viewCounts[i], 'Like Count': likeCounts[i], 'Comment Count': commentCounts[i]})
    except:
        print('Errors writing to  file')

def getVideoInfo(vid: str):
    result = []
    for item in videoCollection.find({"vid": vid}):
        video = {"vid": vid,
                "title": item.get('title')}
        result.append(video)
    return result
        
        

if __name__ == "__main__":
    # for item in testCollection.find({"tags": {"$in": ["Scream"]}}):
    #     print(item)

    client = MongoClient('localhost')
    db = client['dreamcatcher']

    # video's stats collection (view, like, etc on certain date)
    statisticsCollection = db['stats']
    channel = db['channel_stats']
    videoCollection = db['videos']  # video's information (title, published date)

    print(' 1. Find video by ID\n 2. Find all video stats by id \n 3. Retrieve all channel stats \n 4. Quit')
    
    option = int(input("Please choose one of the options above: "))

    if option == 1:
        vid = str(input("Please enter a video id: "))
        print(getVideoInfo(vid))
    elif option == 2:
        vid = str(input("Please enter a video id: "))
        outfile = str(input("Please enter output file name: "))
        retrieveVideoStats(vid, outfile)
    elif option == 3:
        outfile = str(input("Please enter output file name: "))
        retrieveChannelStats(outfile)
    elif option == 4:
        pass
    else:
        print("Invalid input! Quitting...")




   
