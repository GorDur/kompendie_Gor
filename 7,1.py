n = int(input("Ange numer: "))

number = 1 


while number > -1:
    number+=1
    t = n * number 
    print(t) 
    number+=1
    t = n * number 
    print(t) 
    number+=1
    t = n * number 
    print(t) 
    a = input("Vill du fortsätta: ")
    if a == "ja": 
        continue 
    else:
        break