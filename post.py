import requests
import os
import random

PAGE_ID = os.getenv("PAGE_ID")
ACCESS_TOKEN = os.getenv("FB_TOKEN")

POSTS = [
"Man City have 115 charges... And still charging for season tickets WTF",
"Real Madrid from UCL to PDF FC. 50k pages to UEFA, 0 shots on target",
"Arsenal's documentary: How to lead the league for 248 days and win nothing",
"Man United's game plan: 1. Concede 2. Panic 3. Blame manager 4. Repeat",
"Barcelona's bank account is like their defense - Wide open and always leaking",
"Arsenal doesn't bottle water, they bottle leagues"
]

def post_to_facebook():
    message = random.choice(POSTS)
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    data = {"message": message, "access_token": ACCESS_TOKEN}
    r = requests.post(url, data=data)
    print(r.json())

if __name__ == "__main__":
    post_to_facebook()