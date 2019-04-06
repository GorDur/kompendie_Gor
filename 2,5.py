# variabler för antal korv 
a = int(input("vanlig 2 ")) 
b = int(input("vanlig 3 "))
c = int(input("vegan 2 "))
d = int(input("vegan 3 "))

x = (a + b)/8   # antal pack för vanliga korv
x1 =int(x)  
y = (c + d)/8   # antal pack för vegan korv
y1=int(y)

if x1 < 1:  # så att det blir inte mindre än en pack
    x1+=1

if y1 < 1:
    y1+=1

print("vanlig = "+ str(x1) + ","+ "vegan = "+ str(y1))  # output