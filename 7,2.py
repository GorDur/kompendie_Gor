from random import randint
print(".: THE HIGHER LOWER GAME :.")
print("--------------------------")
print("Welcome to The Higher Lower Game. \nI will randomise a number between 0 and 99. \nCan you guess it?")
print("--------------------------")

i = randint(0,99)
a = 0
g = int(input("Your guess > "))


while g > -1:
    a+=1
    if g > i:
        print("Lower")
        g = int(input("Try again > "))
    elif g < i:
        print("Higher")
        g = int(input("Try again > "))
    elif g == i:
        print(str(g) + " is correct! \nIt took you " + str(a) + " guesses. \nGood job!") 
        break


