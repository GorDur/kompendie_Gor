# För att lägga till en parti behöver man ta ett nummer efter det sista partinumret som redan finns
# och lägga till detta på samma sätt som alla andra i hela koden
import ui
from random import randint  # importerar randint
# class för partier
class Parti:    
    def __init__(self,namn,minimum,maximum,inriktning,block,partiledare,won,lose):   # atributer som används
        self.namn = namn    # partiens namn
        # integraler för max och min röster 
        self.minimum = int(minimum) # minimum antal röster
        self.maximum = int(maximum) # maximum antal röster
        self.inriktning = inriktning    # partiens inriktning
        self.block = block  # partiens block
        self.partiledare  = partiledare     # partiledarens namn
        # gör inriktningen till en boolen
        if inriktning == True:  # om det är sant då är det Vänster
            self.inriktning = "Vänster"
        else:   # om det är falskt då är det Höger
            self.inriktning = "Höger"
        self.won = won  # om partiet vinner    
        self.lose = lose  # om partiet förlorar    
# Alla objekter(partier) och deras atributer
parti_1 = Parti("Gröngölingarna","3","12",True,"Småpartierna","Jonas Ostbåge","Vi var helt säkra att vi kommer lyckas!","Iaf vi kämpade bra, men egentligen inte.")
parti_2 = Parti("Partikelpartiet","2","8",True,"Småpartierna","Hans Majonäs","Yesss!","Noooooo!")
parti_3 = Parti("Mälarpartiet","8","18",False,"Småpartierna","Pernilla Godisgorilla","We are the best!","We are the best anyway.")
parti_4 = Parti("Sjörövarpartiet","3","12",False,"Småpartierna","Arja Samerna","Vi kunde göra det!","Livet är svårt.")
parti_5 = Parti("Extremisterna","3","6",False,"Oljeblocket","Lennart Lurig","Ja ja, vi vis+te redan!","Nej men asså...")
parti_6 = Parti("Maskinpartiet","12","22",True,"Oljeblocket","Robert Rostbiff","Nu får ni kola vad hur är det att leva i ett diktatur!!!","Nästa gången får ni se hur är det att leva i ett diktatur.")
parti_7 = Parti("Framtidspartiet","12","18",False,"Oljeblocket","Antwon Släp","Vi hade inte stor chans att vinna men nu har ni ingen chans att överleva!!!","Okej ni fick 4 år till.")
parti_8 = Parti("Allpartiet","15","29",True,"Inget","Dan Dan","Vi älskar alla som röstade på oss, like and subscribe!","Vi hoppades att vi ska vinna, men ändå like and subscribe!")
# Tar en random cifra mellan max och min röster för varje parti
parti_1r = randint(parti_1.minimum,parti_1.maximum)
parti_2r = randint(parti_2.minimum,parti_2.maximum)
parti_3r = randint(parti_3.minimum,parti_4.maximum)
parti_4r = randint(parti_4.minimum,parti_4.maximum)
parti_5r = randint(parti_5.minimum,parti_5.maximum)
parti_6r = randint(parti_6.minimum,parti_6.maximum)
parti_7r = randint(parti_7.minimum,parti_7.maximum)
parti_8r = randint(parti_8.minimum,parti_8.maximum)
# Räcknar max röster för alla partier för att hita befolkningen
befolkning = parti_1.maximum + parti_2.maximum + parti_3.maximum + parti_4.maximum + parti_5.maximum + parti_6.maximum + parti_7.maximum + parti_8.maximum
# Räcknar alla röster som partierna fick
ant_röst = parti_1r + parti_2r + parti_3r + parti_4r + parti_5r + parti_6r + parti_7r + parti_8r
# Delar antal röster som partierna fick med befolkningen för att få hur många procent är det som röstade
b = (ant_röst/befolkning) * 100
# Delar röster som en parti fick med antal röster för att ta reda på hur många procent som röstade på varje parti
parti_1p = int((parti_1r/ant_röst) * 100)
parti_2p = int((parti_2r/ant_röst) * 100)
parti_3p = int((parti_3r/ant_röst) * 100)
parti_4p = int((parti_4r/ant_röst) * 100)
parti_5p = int((parti_5r/ant_röst) * 100)
parti_6p = int((parti_6r/ant_röst) * 100)
parti_7p = int((parti_7r/ant_röst) * 100)
parti_8p = int((parti_8r/ant_röst) * 100)
# Variabler för röster för höger eller vänster
v = parti_1p + parti_2p + parti_6p + parti_8p   # vänster
h = parti_3p + parti_4p + parti_5p + parti_7p   # häger
ui.line(True)
# Array för namn och antal röster för partier
pn = [parti_1.namn,parti_2.namn,parti_3.namn,parti_4.namn,parti_5.namn,parti_6.namn,parti_7.namn,parti_8.namn]
ar = [parti_1p, parti_2p, parti_3p, parti_4p, parti_5p, parti_6p, parti_7p, parti_8p]
# Skriver ut partiernas namn och antal röster i procent om de har mer är 4% av antalet
for f in ar:
    if f >= 4:
        ui.echo(pn[ar.index(f)] + " fick " + str(int(f))+ "%.")
# Variabel för att ta reda på vilken parti fick max röster
m = max(parti_1p, parti_2p, parti_3p, parti_4p, parti_5p, parti_6p, parti_7p, parti_8p)
ui.line()
# Skriver ut den parti som har max röster
ui.header("Största partiet är " + pn[ar.index(max(ar))] + " med " + str(m) + "%.")
# Tar reda på röster som varje block fick
s = parti_1p + parti_2p + parti_3p + parti_4p # småpartier
o = parti_5p + parti_6p + parti_7p  # oljeblocket
i = parti_8p    # inget block
ui.line()
# Tar reda på vilket block som har max röster
if s > o and s > i:
    ui.header("Största blocket är Småpartierna med " + str(int(s)) + "%")
if o > s and o > i:
    ui.header("Största blocket är Oljeblocket med " + str(int(o)) + "%")
ui.line()
# Tar reda på vilken inriktning som har fler röster
if v > h:
    ui.header( "De flesta har valt vänster med " + str(int(v)) + "%." )
elif v < h:
    ui.header( "De flesta har valt höger med " + str(int(h)) + "%." )
else:
    ui.header("Det blev lika många röster för båda vänster och höger.")
ui.line()
ui.header(str(int(b)) + "% "+ "av befolkningen har röstat.") 
ui.line()
# Partiledarnas tal i fal om de vann eller förlorade
if parti_1p == m:
    ui.echo(parti_1.partiledare + ": " + parti_1.won)
else:
    ui.echo(parti_1.partiledare + ": " + parti_1.lose)
if parti_2p == m:
    ui.echo(parti_2.partiledare + ": " + parti_2.won)
else:
    ui.echo(parti_2.partiledare + ": " + parti_2.lose)
if parti_3p == m:
    ui.echo(parti_3.partiledare + ": " + parti_3.won)
else:
    ui.echo(parti_3.partiledare + ": " + parti_3.lose)
if parti_4p == m:
    ui.echo(parti_4.partiledare + ": " + parti_4.won)
else:
    ui.echo(parti_4.partiledare + ": " + parti_4.lose)
if parti_5p == m:
    ui.echo(parti_5.partiledare + ": " + parti_5.won)
else:
    ui.echo(parti_5.partiledare + ": " + parti_5.lose)
if parti_6p == m:
    ui.echo(parti_6.partiledare + ": " + parti_6.won)
else:
    ui.echo(parti_6.partiledare + ": " + parti_6.lose)
if parti_7p == m:
    ui.echo(parti_7.partiledare + ": " + parti_7.won)
else:
    ui.echo(parti_7.partiledare + ": " + parti_7.lose)
if parti_8p == m:
    ui.echo(parti_8.partiledare + ": " + parti_8.won)
else:
    ui.echo(parti_8.partiledare + ": " + parti_8.lose)