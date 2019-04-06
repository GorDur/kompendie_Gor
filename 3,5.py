male =[
    "Erik",
    "Lars",
    "Karl",
    "Andreas",
    "Johan"
    ]

female =[
    "Maria",
    "Anna",
    "Margareta",
    "Elisabeth",
    "Eva"
]

x = input("vilket name?  ") # input för ett namn

male.remove(x)  # namnet tas bort från män
print(male) # skriver ut män
female.remove(x)    # namnet tas bort från kvinnor
print(female)   # skriver ut kvinnor
