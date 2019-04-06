registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]  # array för registrerade namn
avanmälningar = ["Anna", "Erik", "Karl"]    # array för avanmälningar

for namn in avanmälningar:  # for loop 
    if namn in registrerade:    # om namnet är i registrerade 
        registrerade.remove(namn)   # då tas det bort

print(registrerade)