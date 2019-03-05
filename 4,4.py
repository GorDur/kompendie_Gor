förnamn = ["Maria", "Erik", "Karl"]
efternamn = ["Svensson", "Karlsson", "Andersson"]

for namn in förnamn:
    for efnamn in efternamn:
        person = str(namn) + " " + str(efnamn)
        print(person)

