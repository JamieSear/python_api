import requests
from repos import Repos


def fetch_user_data(username):
    req = requests.get(f'https://api.github.com/users/{username}/repos')
    for data in req.json():
        Repos(data)
