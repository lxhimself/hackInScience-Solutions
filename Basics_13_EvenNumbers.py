def print_even_numbers(start, stop):
    for i in range(start, stop):
        if  (i % 2) == 0:
            print(i)


start = int(input("Startnummer: "))
stop = int(input("Stopnummer: "))

print_even_numbers(start,stop)

