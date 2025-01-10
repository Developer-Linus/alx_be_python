# Define Global Variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp_input = float(input("Enter the temperature to convert: "))
temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
        fahrenheit = temp_input
        if fahrenheit:
                temp_celsius = FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)
                print(f"{fahrenheit}F is {temp_celsius}°C")
        else:
                print("Invalid temperature. Please enter a numeric value.")

    
# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
        celsius = temp_input
        if celsius:
                temp_fahrenheit = ((celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
                print(f"{celsius}°C is {temp_fahrenheit}F")
        else:
                print("Invalid temperature. Please enter a numeric value.")

if temp_state == "F":
        convert_to_celsius(fahrenheit = temp_input)
elif temp_state == "C":
        convert_to_fahrenheit(celsius=temp_input)
else:
        print("Invalide temperature unit.")
        
        


