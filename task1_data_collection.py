#requirments
import requests 
import time
import json
import os
from datetime import datetime
#1.top story ids
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
#checking request successful
if  response.status_code != 200:
    print("Failed story ids")
    exit()
ids = response.json()
#first 120 ids
ids = ids[:120]
#store all stories
total_stories = []
#looping ids and fetch each story
for id_story in ids:
    try:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{id_story}.json"
        item_response = requests.get(item_url)
        if item_response.status_code != 200:
            print(f"Skipping id{id_story}")
            continue
        story = item_response.json()
        #title skip
        if story is None or "title" not in story:
            continue
        title = story.get("title","").lower()
        #giving category
        if any(word in title for word in ["ai", "tech","software","computer","data"]):
            category = "technology"
        elif any(word in title for word in ["war","government","election","climate"]):
            category = "worldnews"
        elif any(word in title for word in ["nfl","nba","fifa","game","team"]):
            category = "sports"
        elif any(word in title for word in ["science","research","space","nasa"]):
            category = "science"
        elif any(word in title for word in ["movie","music","film","netflix"]):
            category = "entertainment"
        else:
            category = "others"
            #required fields
        story_data = {
                "post_id":story.get("id"),
                "title":story.get("title"),
                "category":category,
                "score":story.get("score",0),
                "num_comments":story.get("descendants",0),
                "author":story.get("by"),
                "collected_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            #add to list
        total_stories.append(story_data)
    except Exception as e:
        print(f"Error with id{id_story}:{e}")
#data folder 
if not os.path.exists("data"):
    os.makedirs("data")
#JSON file saveing
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
with open(filename,"w",encoding="utf-8") as f:
    json.dump(total_stories,f,indent=4)
#output
print(f"Collected {len(total_stories)} stories. Saved to {filename}")