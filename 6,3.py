import requests
url= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" 
r = requests.get(url) 
R = r.json()
print ("--- ARTIST DB -- \nAriana Grande \nAvicii \nBlink -182 \nBrad Paisley \nEd Sheeran \nImagine Dragons \nMaroon 5 \nScorpions")
print ("----------------")
N = input("Select artist: \n> ")
a = N.title()

for S in R["artists"]:
    if (a == S["name"]):
        c = S["id"]

url1= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + c
r1 = requests.get(url1) 
R1 = r1.json()

e = R1["artist"]["genres"]
f = R1["artist"]["years_active"]
h = R1["artist"]["members"]


i=""
i1=""
i2=""

for k in e:
    i += k +", "

for k1 in f:
    i1 += k1 +", "

for k2 in h:
    i2 += k2 +", "

print("Genres: " + i + "\nActive: "+ i1 +"\nMembers: " + i2)
print("----------------")