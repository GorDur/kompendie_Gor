Norden = ["Danmark","Finland","Island","Norge","Sverige"]
Storbritanien = ["England","Nordirland","Skottland","Wales"]

n = input("Ange landet: ")
name = n.capitalize()

if name or n in Norden:
    print("Landet tillhör till Norden")
elif name or n in Storbritanien:
    print("Landet tillhör till Storbritanien")
else:
    print("error")