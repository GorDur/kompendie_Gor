def line(dots = False):
    if dots == True:
        print("******************************")
    elif dots == False:
        print("-----------------------------")
    
def header(text):
    x = text.center(28, " ")
    print ("|" + x + "|")

def echo(text):
    print("| " + text)

def prompt(text):
    a = input("| " + text + " > ")
    return a

def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")