a = int(input("Ange distans > ")) 
b = input("Välj enhet > ")

def km_to_miles(dist): 
    return dist * 0.621371

def miles_to_km(dist):
    return dist / 0.621371

num1 = km_to_miles(a)
num2 = miles_to_km(a)

if b == "km":
    print( str(a) + " km motsvarar " + str(num1) + " miles.")
elif b == "miles":
    print(str(a) + " miles motsvarar " + str(num2) + " km.")