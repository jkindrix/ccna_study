import random

while True:
    print("\nPlease select a mode:\n")
    print("a.) Network Bits")
    print("b.) Left-side Bits")
    print("c.) Right-side Bits")
    print("d.) All Bits\n")

    selection = input("Selection: ")

    if selection.lower() in ('a', 'b', 'c', 'd'):
        break
    else:
        continue

print("\nWrite the following binary numbers in decimal form.")

while True:
    if selection.lower() == 'a':
        decimal_number = random.choice([0, 128, 192, 224, 240, 248, 252, 254, 255])
    elif selection.lower() == 'b':
        decimal_number = random.randrange(0, 240, 16)
    elif selection.lower() == 'c':
        decimal_number = random.randint(0, 15)
    elif selection.lower() == 'd':
        decimal_number = random.randint(0, 255)

    binary_number = format(decimal_number, '08b')

    while True:
        try:
            answer = int(input(f"{binary_number} -> "))
        except ValueError:
            print("Please enter an integer between 0 - 255.\n")
            continue

        if answer < 0 or answer > 255:
            print("Please enter an integer between 0 - 255.\n")
            continue
        else:
            break

    if answer == decimal_number:
        print("Great Job!\n")
    else:
        print(f"Sorry. The answer was {decimal_number}\n")