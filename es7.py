import sys

successivo = 0
precedente = 0
doppio = 0
metà = 0

if len(sys.argv) != 3:
    print("Inserire solo 2 parametri")
else:
    lettera = sys.argv[1].upper()
    a = float(sys.argv[2])
    if lettera == "S":
        successivo = a + 1
        print(f"Il successivo é {successivo}")
    elif lettera == "P":
        precedente = a - 1
        print(f"Il precedente é {precedente}")
    elif lettera == "D":
        doppio = a * 2
        print(f"Il doppio é {doppio}")
    elif lettera == "M":
        metà = a / 2
        print(f"La metà é {metà}")
    else:
        print(f"Carattere errato!")
