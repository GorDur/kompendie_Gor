import requests # importerar vivliotek
url= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"    # url som ska användas
r = requests.get(url)   # får urlen
R = r.json()    # gör om till json fill
print ("--- ARTIST DB -- \nAriana Grande \nAvicii \nBlink -182 \nBrad Paisley \nEd Sheeran \nImagine Dragons \nMaroon 5 \nScorpions")
print ("----------------")
N = input("Select artist: \n> ")
a = N.title()   # gör så att namnet ska skrivas med stor bokstav

c = ""  #tomt variabel

for S in R["artists"]:  # kollar efter det speciela artisten i listan och hämtar hens id
    if (a == S["name"]):    
        c = S["id"]

url1= "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + c    # samma url fast med id
r1 = requests.get(url1) # får urlen
R1 = r1.json()  # gör om till json fill

e = R1["artist"]["genres"]  # variabel för genre
f = R1["artist"]["years_active"]    # för aktiva år 
h = R1["artist"]["members"] # för medlemar 

i="" 
i1=""
i2=""

for k in e:     # variabel som addar till sig varje värde från genre
    i += k +", "

for k1 in f:    # variabel som addar till sig varje värde från years active
    i1 += k1 +", "

for k2 in h:    # variabel som addar till sig varje värde från members
    i2 += k2 +", "

print("Genres: " + i + "\nActive: "+ i1 +"\nMembers: " + i2)    # skriver ut svaret
print("----------------")