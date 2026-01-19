def to_decimal(number, base):
    """Convert any base number to decimal"""
    return int(number, base)


def from_decimal(number, base):
    """Convert decimal to any base"""
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:].upper()
    else:
        return str(number)


def convert_number(number, from_base, to_base):
    """Convert number from one base to another"""
    decimal_value = to_decimal(number, from_base)
    return from_decimal(decimal_value, to_base)


def menu():
    print("\nNUMBER SYSTEM CONVERTER")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Octal to Decimal")
    print("4. Decimal to Octal")
    print("5. Hexadecimal to Decimal")
    print("6. Decimal to Hexadecimal")
    print("7. Binary to Octal")
    print("8. Binary to Hexadecimal")
    print("9. Octal to Binary")
    print("10. Hexadecimal to Binary")
    print("0. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "0":
        break

    number = input("Enter number: ")

    try:
        if choice == "1":
            print("Decimal:", convert_number(number, 2, 10))
        elif choice == "2":
            print("Binary:", convert_number(number, 10, 2))
        elif choice == "3":
            print("Decimal:", convert_number(number, 8, 10))
        elif choice == "4":
            print("Octal:", convert_number(number, 10, 8))
        elif choice == "5":
            print("Decimal:", convert_number(number, 16, 10))
        elif choice == "6":
            print("Hexadecimal:", convert_number(number, 10, 16))
        elif choice == "7":
            print("Octal:", convert_number(number, 2, 8))
        elif choice == "8":
            print("Hexadecimal:", convert_number(number, 2, 16))
        elif choice == "9":
            print("Binary:", convert_number(number, 8, 2))
        elif choice == "10":
            print("Binary:", convert_number(number, 16, 2))
        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid number for selected base!")
