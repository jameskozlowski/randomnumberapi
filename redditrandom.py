import random
import hashlib
import requests
import requests.auth
import hashlib
from random import Random


class RedditRandom(random.Random):

    def __init__(self, seed_value=None):
        random.Random.__init__(self, seed_value)
        self.seeds = []

    def randint(self, min, max):
        if not self.seed or len(self.seeds) <= 0:
            self.seeds = self.getRedditComments()

        if self.seeds and len(self.seeds) > 0:
            h = int(hash(self.seeds.pop()['data']['body']))
            self.seed(h)

        return random.Random.randint(self, min, max)

    def getRedditComments(self):
        headers = {"User-Agent": "randomnuumberapi/0.1 by JK"}
        response = requests.get("https://api.reddit.com/r/all/comments/.json?limit=100", headers=headers)
        seeds = response.json()['data']['children']
        return seeds
