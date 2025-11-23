# Python CLI Unit Converter

A simple command-line interface (CLI) application for converting between different units of measurement including weight, temperature, and length/height.

## Features

### 1. Weight Conversion (Fully Implemented)
Converts between:
- Stones
- Pounds
- Kilograms

Conversion rates used:
- 1 stone = 14 pounds
- 1 stone = 7 kg
- 1 kg = 2 pounds

### 2. Temperature Conversion (Skeleton/Framework)
The application provides a framework for temperature conversions:
- Celsius to Fahrenheit (and vice versa)
- Celsius to Kelvin (and vice versa)
- Fahrenheit to Kelvin (and vice versa)

**Note**: The temperature conversion functions are provided as skeletons with TODO comments and conversion formulas for you to implement.

### 3. Length/Height Conversion (Skeleton/Framework)
The application provides a framework for length conversions:
- Centimeters to Inches (and vice versa)

**Note**: The length conversion functions are provided as skeletons with TODO comments and conversion formulas for you to implement.

## Installation

No additional dependencies required. The application uses only Python 3 standard library.

## Usage

Run the application:
```bash
python3 unit_converter.py
```

Follow the interactive prompts to:
1. Select the type of conversion (weight, temperature, or length)
2. Choose the specific conversion
3. Enter the value to convert
4. View the result

## Example

```
Welcome to the CLI Unit Converter!

==================================================
                CLI Unit Converter                
==================================================

Select conversion type:
1. Weight (stones, pounds, kilograms)
2. Temperature (Celsius, Fahrenheit, Kelvin)
3. Length/Height (centimeters, inches)
4. Exit
==================================================

Enter your choice (1-4): 1

Weight Conversion
Available units: stones, pounds, kg
Enter value: 1
From unit (stones/pounds/kg): stones
To unit (stones/pounds/kg): kg

1.0 stones = 7.00 kg
```

## Implementation Notes

### Weight Conversion Logic
The weight conversion uses pounds as an intermediate unit for all conversions, ensuring accuracy across all conversion pairs.

### Temperature and Length Conversions
These are provided as function skeletons with:
- Clear function names
- Descriptive docstrings
- TODO comments
- Conversion formulas in comments
- Placeholder `pass` statements for you to implement

You can implement these functions by replacing the `pass` statement with the actual conversion logic.

## File Structure

- `unit_converter.py` - Main application file containing all conversion logic and CLI interface

## License

Open source - feel free to use and modify as needed.