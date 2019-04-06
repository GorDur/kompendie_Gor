name = input("Ange ditt namn: ")    
age = int(input("Ange din ålder: "))

ages =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,]
timmar = [14,13,12,11.5,11,11,11,11.5,10,10,10,9.5,9,9,9,8.5,8]

if age in ages: # om age är i arrayen ages då skriver ut det här
    print("Hallå " + name + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(age) + ") sova minst " + str(timmar[age - 1]) + " timmar per natt.")
else:   # annars det här
    print("Hallå " + name + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(age) + ") sova minst 8 timmar per natt.")