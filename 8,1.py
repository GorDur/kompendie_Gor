def km_to_miles(dist): # funktion för km till miles
    return str(dist * 0.621371) + "miles"

def miles_to_km(dist):  # funktion för miles till km
    return str(dist / 0.621371) + "km"

a = input("Ange distans > ") # input

if "km" in a:   # om värdet är i km 
    s = km_to_miles(float(a.strip("km")))   # används första funktionen
elif "miles" in a:  # om värdet är i miles används andra funktionen
    s = miles_to_km(float(a.strip("miles")))    

print(a + " är " + s)   # output