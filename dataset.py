from config import *
import requests
import re
from nlptoolsjp.file_system import file_create


def comment_get(url):
    if "?v=" not in url:
        return 0
    video_id = url.split('?v=')[1]
    pattern = re.compile(r'&\S*')
    video_id = pattern.sub('',video_id)
    URL = "https://www.googleapis.com/youtube/v3/"
    next_page = None
    comment_params = {
    "key": KEY,
    "part": "snippet",
    "videoId": video_id,
    "order": "relevance",
    "textFormat": "plaintext",
    "maxResults": 100,
  }
    main_params = {
        "key":KEY,
        "part": "snippet",
        "id":video_id
    }
    dict_data = {'videoid':video_id,'title':None,'channel':None,'comment':[]}
    main_response = requests.get(URL+"videos",params=main_params).json()
    try:
        main_data = main_response["items"][0]["snippet"]
    except:
        return 0
    dict_data['title']  = re.sub(r'\.|\\|/','',main_data["title"])
    dict_data['channel'] = main_data["channelTitle"]
    for i in range(50):
        if next_page is not None:
            comment_params["pageToken"] = next_page
        try:
            response = requests.get(URL + "commentThreads", params = comment_params)
            response_dict = response.json()
        except:
            return 0
        for data in response_dict["items"]:
            dict_data["comment"].append(data['snippet']['topLevelComment']['snippet']['textOriginal'])
        if "nextPageToken" in response_dict:
            next_page = response_dict["nextPageToken"]
        else:
            break
    file_create(dict_data, file_path = f'comment_data/{dict_data["title"]}.json')
    return dict_data

if __name__=="__main__":
    url1 = "https://www.youtube.com/watch?v=6LcrMMP4pDg"
    url2 = "https://www.youtube.com/watch?v=wWO9s7VDIRI&list=RDGMEMXdNDEg4wQ96My0DhjI-cIgVMSvFRRs5DsHk&index=10"
    a = comment_get(url2)
    print(a)
