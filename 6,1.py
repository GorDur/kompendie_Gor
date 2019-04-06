import requests # importerar requests
number = int(input("skriv ett positivt heltal: "))  # variabel för numer
url = "http://77.238.56.27/examples/numinfo/?integer=" + str(number)    # url som inkluderar också numret som vi skrev
r = requests.get(url) 
response_dictionary = r.json() 
# Nu inneh˚aller response_dictionary objektet vi vi hämtade från API

if response_dictionary["even"]==True:   # om numret är even 
    print("even")   
else:
    print("not even")
if response_dictionary["prime"]==True:  # om den är prime
    print ("prime")
else:
    print("not prime")
print ("factors: " + str(response_dictionary["factors"])) # skriver ut  alla factors för numret 
