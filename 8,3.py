import ui   # importerar ui
# använder funktioner från ui
ui.line()   # gör linje 
ui.header("EXEMPEL")    # skriver ut i mitten och med | på sidorna
ui.line(True)   # gör linje av sjärnor
ui.echo("Detta är ett exempel på hur")   # skriver ut med en | från början
ui.echo("ett grännsnitt kan se ut.") 
ui.line() 
ui.header("..vad vill du göra?") 
ui.line() 
ui.echo("A | Visa inköpslista") 
ui.echo("B | Lägg till vara") 
ui.echo("C | Ta bort vara") 
ui.echo("X | Stäng programmet") 
ui.line() 
ui.prompt("Val")    # finns möjlighet att göra input