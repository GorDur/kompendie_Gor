import web  # importerar web 

s = web.get("https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/Stockholm")    # urlen används genom funktionen get från web 
print(s)    # output