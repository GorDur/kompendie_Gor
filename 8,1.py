def km_to_miles(dist): # funktion för km till miles
    return str(dist * 0.621371) + "miles"

def miles_to_km(dist):  #funktion för miles till km
    return str(dist / 0.621371) + "km"

a = input("Ange distans > ") # input

if "km" in a:
    s = km_to_miles(float(a.strip("miles")))
elif "miles" in a:
    s = miles_to_km(float(a.strip("km")))

print(a + " är " + s)