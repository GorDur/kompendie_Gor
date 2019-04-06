tal = range(501)    # längden 

sum = 0 # summan är 0

for i in tal:   
    if i % 2 != 0:  # om talet är jämn
        sum += i    # då adderas det till summan
    else:
        continue    # annars tas nästa

print (sum)
