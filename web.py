import requests # importerar requests

def get(url):   # definerar get
    r = requests.get(url)   # får urlen 
    R = r.json()    # gör om till json fill 
    return R    # returnerar