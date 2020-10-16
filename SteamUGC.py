import requests
import re

types = {
    'screenshots': 5,
    'videos': 4,
    'images': 3,
    'myworkshopfiles': 0,
}


def fetch_target_ugc(target):
    results = []
    for t in types:
        page = 1
        while True:
            resp = requests.post("https://steamcommunity.com/%s/%s/" % (target, t), data={
                "appid": 0,
                "p": page,
                "privacy": 999,
                "content": 1,
                "sort": "newestfirst",
                "view": "imagewall",
            })
            r = re.findall('data-publishedfileid="(\\d+)"', resp.text)
            for item in r:
                results.append((types[t], int(item)))
            page += 1
            if len(r) == 0:
                break
    return results
