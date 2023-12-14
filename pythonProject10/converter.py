def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462
def pounds_to_kilograms(pounds):
    return pounds / 2.20462
def get_user_input():
    print("Choose an option:")
    print("1. Temperature Converter (Celsius ⇔ Fahrenheit)")
    print("2. Length Converter (Meters ⇔ Feet)")
    print("3. Weight Converter (Kilograms ⇔ Pounds)")
    choice = input("Enter your choice (1/2/3): ")
    return choice
while True:
    choice = get_user_input()
    if choice == '1':
        try:
            value = float(input("Enter temperature value: "))
            source_unit = input("Enter source unit (C/F): ").upper()
            target_unit = input("Enter target unit (C/F): ").upper()
            if source_unit == 'C' and target_unit == 'F':
                result = celsius_to_fahrenheit(value)
                print(f"{value} Celsius is equal to {result} Fahrenheit")
            elif source_unit == 'F' and target_unit == 'C':
                result = fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is equal to {result} Celsius")
            else:
                print("Unsupported unit conversion.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '2':
        try:
            value = float(input("Enter length value: "))
            source_unit = input("Enter source unit (M/F): ").upper()
            target_unit = input("Enter target unit (M/F): ").upper()
            if source_unit == 'M' and target_unit == 'F':
                result = meters_to_feet(value)
                print(f"{value} Meters is equal to {result} Feet")
            elif source_unit == 'F' and target_unit == 'M':
                result = feet_to_meters(value)
                print(f"{value} Feet is equal to {result} Meters")
            else:
                print("Unsupported unit conversion.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '3':
        try:
            value = float(input("Enter weight value: "))
            source_unit = input("Enter source unit (K/P): ").upper()
            target_unit = input("Enter target unit (K/P): ").upper()
            if source_unit == 'K' and target_unit == 'P':
                result = kilograms_to_pounds(value)
                print(f"{value} Kilograms is equal to {result} Pounds")
            elif source_unit == 'P' and target_unit == 'K':
                result = pounds_to_kilograms(value)
                print(f"{value} Pounds is equal to {result} Kilograms")
            else:
                print("Unsupported unit conversion.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")