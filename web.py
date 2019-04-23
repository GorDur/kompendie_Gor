import requests

def get(url):
    r = requests.get(url) 
    R = r.json()
    return R