import sys
if len(sys.argv)!=2:
    print("python3 es5.py <parametro>")
else:
    number = int(sys.argv[1])
    fatt = 1
    for i in range(number, 0, -1):
        fatt = fatt * i
    print(f"Il fattoriale di {number} é {fatt}")