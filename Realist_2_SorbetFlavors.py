FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]



for i in FLAVORS:
    for x in FLAVORS:
        if x != i:
           if i < x:
            print(i + "," + " " + x)
            