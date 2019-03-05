registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar = ["Anna", "Erik", "Karl"]

for namn in avanmälningar:
    if namn in registrerade:
        registrerade.remove(namn)



print(registrerade)