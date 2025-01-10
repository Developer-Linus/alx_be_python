# Define Global Variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program to handle user input
def main():
    temp_input = float(input("Enter the temperature to convert: "))
    temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temp_state == "F":
        temp_celsius = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {temp_celsius:.2f}°C")
    elif temp_state == "C":
        temp_fahrenheit = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {temp_fahrenheit:.2f}°F")
    else:
        print("Invalid input. Please specify C for Celsius or F for Fahrenheit.")

# Run the main function
if __name__ == "__main__":
    main()
