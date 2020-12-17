import sys

if len(sys.argv) != 4:
    print("Inserire solo 3 parametri")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    if a > b and a > c:
        print(f"Il max é {a}")
    elif b > a and b > c:
        print(f"Il max é {b}")
    else:
        print(f"Il max é {c}")
