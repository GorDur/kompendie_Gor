from random import randint  # importrar randint
print(".: THE HIGHER LOWER GAME :.")
print("--------------------------")
print("Welcome to The Higher Lower Game. \nI will randomise a number between 0 and 99. \nCan you guess it?")
print("--------------------------")

i = randint(0,99)   # random värde mellan 0 och 99
a = 0   # variabel för hur många gånger har man provat
g = int(input("Your guess > ")) # vilket värde gissar man

while g > -1:   # loopen körs hela tidden
    a+=1    # varje gång som loopen körs adderas 1 till hur många gånger har man provat
    if g > i:       # om gissningen är större än värdet
        print("Lower")  
        g = int(input("Try again > "))  # försöker igen
    elif g < i: # om gissningen är mindre än värdet
        print("Higher")
        g = int(input("Try again > "))
    elif g == i:    # om gissningen är rätt
        print(str(g) + " is correct! \nIt took you " + str(a) + " guesses. \nGood job!")    
        break   # stop


