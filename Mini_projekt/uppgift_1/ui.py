def line(dots = False): # säger att dots är false som default
    if dots == True:    # om dots är sant
        print("******************************************************************************************************************") # skriver ut sjärnor
    elif dots == False: # om falsk skriver ut linje
        print("------------------------------------------------------------------------------------------------------------------")
    
def header(text):   
    x = text.center(28, " ")    # texten i header ska varar centrerat 
    print ("|" + x + "|")   # med | på sidorna

def echo(text): 
    print("| " + text)  # texten för echo ska skrivas ut efter |    

def prompt(text):
    a = input("| " + text + " > ")  # prompt ska ha möjlighet för input också
    return a    # returnerar 

def clear():    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # skulle ta bort men skapar många toma rader så att det ser ut lik som man har tagit bort) 