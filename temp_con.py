def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Application")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        celsius = float(input("Enter the Celsius value: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    elif choice == '2':
        fahrenheit = float(input("Enter the Fahrenheit value: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
