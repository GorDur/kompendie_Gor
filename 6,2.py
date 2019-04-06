import requests
stad = input ("Enter the name of the city \nfor which you want forecasts: \n> ")
url= "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + stad
r = requests.get(url) 
a = r.json()

print("--------------------- \n      FORECASTS \n********************** \n" )
for S in a["forecasts"]:
    print(S["date"] +"   " + S["forecast"])
