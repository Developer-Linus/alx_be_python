# Define Global Variables
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

temperature_to_convert = float(input("Enter the temperature to convert: "))
temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
        fahrenheit = temperature_to_convert
        temp_celsius = FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
        print(f"{fahrenheit} F is {temp_celsius} °C")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
        celsius = temperature_to_convert
        temp_fahrenheit = ((celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
        print(f"{celsius} °C is {temp_fahrenheit} F")

if temp_state == "F":
        convert_to_celsius(fahrenheit=temperature_to_convert)
elif temp_state == "C":
        convert_to_fahrenheit(celsius=temperature_to_convert)
else:
        print("Invalid temperature. Please enter a numeric value.")
