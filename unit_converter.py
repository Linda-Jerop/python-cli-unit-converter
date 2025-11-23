#!/usr/bin/env python3
"""
CLI Unit Converter
Converts between different units of weight, temperature, and length.
"""


def convert_weight(value, from_unit, to_unit):
    """
    Convert weight between stones, pounds, and kilograms.
    Conversion rates:
    - 1 stone = 14 pounds
    - 1 stone = 7 kg
    - 1 kg = 2 pounds
    """
    # First convert to pounds as intermediate unit
    if from_unit == "stones":
        pounds = value * 14
    elif from_unit == "pounds":
        pounds = value
    elif from_unit == "kg":
        pounds = value * 2
    else:
        return None
    
    # Then convert from pounds to target unit
    if to_unit == "stones":
        return pounds / 14
    elif to_unit == "pounds":
        return pounds
    elif to_unit == "kg":
        return pounds / 2
    else:
        return None


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    TODO: Add your conversion formula here
    Formula: F = (C × 9/5) + 32
    """
    # Add your implementation here
    pass


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    TODO: Add your conversion formula here
    Formula: C = (F - 32) × 5/9
    """
    # Add your implementation here
    pass


def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    TODO: Add your conversion formula here
    Formula: K = C + 273.15
    """
    # Add your implementation here
    pass


def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    TODO: Add your conversion formula here
    Formula: C = K - 273.15
    """
    # Add your implementation here
    pass


def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    TODO: Add your conversion formula here
    Formula: K = (F - 32) × 5/9 + 273.15
    """
    # Add your implementation here
    pass


def kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    TODO: Add your conversion formula here
    Formula: F = (K - 273.15) × 9/5 + 32
    """
    # Add your implementation here
    pass


def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    TODO: Add your conversion formula here
    Formula: inches = cm / 2.54
    """
    # Add your implementation here
    pass


def inches_to_cm(inches):
    """
    Convert inches to centimeters.
    TODO: Add your conversion formula here
    Formula: cm = inches × 2.54
    """
    # Add your implementation here
    pass


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("CLI Unit Converter".center(50))
    print("="*50)
    print("\nSelect conversion type:")
    print("1. Weight (stones, pounds, kilograms)")
    print("2. Temperature (Celsius, Fahrenheit, Kelvin)")
    print("3. Length/Height (centimeters, inches)")
    print("4. Exit")
    print("="*50)


def weight_conversion_menu():
    """Handle weight conversion."""
    print("\nWeight Conversion")
    print("Available units: stones, pounds, kg")
    
    try:
        value = float(input("Enter value: "))
        from_unit = input("From unit (stones/pounds/kg): ").strip().lower()
        to_unit = input("To unit (stones/pounds/kg): ").strip().lower()
        
        result = convert_weight(value, from_unit, to_unit)
        
        if result is not None:
            print(f"\n{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            print("Invalid unit specified!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def temperature_conversion_menu():
    """Handle temperature conversion."""
    print("\nTemperature Conversion")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    try:
        choice = input("Select conversion (1-6): ").strip()
        value = float(input("Enter value: "))
        
        if choice == "1":
            result = celsius_to_fahrenheit(value)
            print(f"\n{value}°C = {result}°F" if result is not None else "Not implemented yet!")
        elif choice == "2":
            result = fahrenheit_to_celsius(value)
            print(f"\n{value}°F = {result}°C" if result is not None else "Not implemented yet!")
        elif choice == "3":
            result = celsius_to_kelvin(value)
            print(f"\n{value}°C = {result}K" if result is not None else "Not implemented yet!")
        elif choice == "4":
            result = kelvin_to_celsius(value)
            print(f"\n{value}K = {result}°C" if result is not None else "Not implemented yet!")
        elif choice == "5":
            result = fahrenheit_to_kelvin(value)
            print(f"\n{value}°F = {result}K" if result is not None else "Not implemented yet!")
        elif choice == "6":
            result = kelvin_to_fahrenheit(value)
            print(f"\n{value}K = {result}°F" if result is not None else "Not implemented yet!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def length_conversion_menu():
    """Handle length/height conversion."""
    print("\nLength/Height Conversion")
    print("Available conversions:")
    print("1. Centimeters to Inches")
    print("2. Inches to Centimeters")
    
    try:
        choice = input("Select conversion (1-2): ").strip()
        value = float(input("Enter value: "))
        
        if choice == "1":
            result = cm_to_inches(value)
            print(f"\n{value} cm = {result} inches" if result is not None else "Not implemented yet!")
        elif choice == "2":
            result = inches_to_cm(value)
            print(f"\n{value} inches = {result} cm" if result is not None else "Not implemented yet!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def main():
    """Main function to run the CLI unit converter."""
    print("Welcome to the CLI Unit Converter!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            weight_conversion_menu()
        elif choice == "2":
            temperature_conversion_menu()
        elif choice == "3":
            length_conversion_menu()
        elif choice == "4":
            print("\nThank you for using the CLI Unit Converter!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
