# Define Global Variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program for user interaction
def main():
    try:
        # Prompt for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temp_input = float(temp_input)

        # Prompt for unit input
        temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if temp_state not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        # Perform conversion based on the unit
        if temp_state == "F":
            temp_celsius = convert_to_celsius(temp_input)
            print(f"{temp_input:.1f}°F is {temp_celsius:.1f}°C")
        elif temp_state == "C":
            temp_fahrenheit = convert_to_fahrenheit(temp_input)
            print(f"{temp_input:.1f}°C is {temp_fahrenheit:.1f}°F")

    except ValueError as e:
        print(e)

# Run the main program
if __name__ == "__main__":
    main()
