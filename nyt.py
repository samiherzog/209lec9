import requests
import secrets
import json


def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories)
