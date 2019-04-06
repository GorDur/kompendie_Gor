Norden = ["Danmark","Finland","Island","Norge","Sverige"]
Storbritanien = ["England","Nordirland","Skottland","Wales"]

n = input("Ange landet: ")  # variabeln
name = n.capitalize()   # gör så att första blir stor bokstav 

if name or n in Norden: # frågar efter båda variabler eftersom vi vet inte hur skrev man namnet 
    print("Landet tillhör till Norden")
elif name or n in Storbritanien:    # samma här
    print("Landet tillhör till Storbritanien")
else:   # om namnet finns inte i båda arrayer då skriver programet ut error
    print("error")