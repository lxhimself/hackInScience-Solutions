import sys 

try:
    OP1 = int(sys.argv[1])
    OP2 = int(sys.argv[2])
    ergebnis = OP1 + OP2
    print(ergebnis)

except:
    print("usage: python3 solution.py OP1 OP2")

