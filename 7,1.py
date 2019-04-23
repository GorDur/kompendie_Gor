n = int(input("Ange numer: "))  # integral input

number = 1  # variabel som är lika medd 1 från början

while number > -1:  # gör så att loopen körs hela tiden
    number+=1          # kör samma sak tre gånger
    t = n * number 
    print(t) 
    number+=1
    t = n * number 
    print(t) 
    number+=1
    t = n * number 
    print(t) 
    a = input("Vill du fortsätta: ")    # frågar om att fortsätta
    if a == "ja":   # om det är ja då fortsätts 
        continue 
    else:   # annars stoppar
        break