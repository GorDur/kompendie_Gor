förnamn = ["Maria", "Erik", "Karl"]
efternamn = ["Svensson", "Karlsson", "Andersson"]

for namn in förnamn:
    for efnamn in efternamn:    # om varibeln efnamn finns i arrayen efternamn
        person = str(namn) + " " + str(efnamn)  # då personen blir lika med namn + efnamn
        print(person)   # skriver ut personen

