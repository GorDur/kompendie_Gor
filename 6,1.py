import requests
number = int(input("skriv ett positivt heltal: "))
url = "http://77.238.56.27/examples/numinfo/?integer=" + str(number) 
r = requests.get(url) 
response_dictionary = r.json() 
# Nu inneh˚aller response_dictionary objektet vi 
# # h¨amtade fr˚an API:et. 


if response_dictionary["even"]==True:
    print("even")
else:
    print("not even")
if response_dictionary["prime"]==True:
    print ("prime")
else:
    print("not prime")
print ("factors: " + str(response_dictionary["factors"]))
