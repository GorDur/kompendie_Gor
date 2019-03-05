a = int(input("vanlig 2 "))
b = int(input("vanlig 3 "))
c = int(input("vegan 2 "))
d = int(input("vegan 3 "))

x = (a + b)/8
x1 =int(x)
y = (c + d)/8
y1=int(y)

if x1 < 1:
    x1+=1

if y1 < 1:
    y1+=1

print("vanlig = "+ str(x1) + ","+ "vegan = "+ str(y1))