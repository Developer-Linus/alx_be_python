# Define Global Variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5




# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
        temp_input = float(input("Enter the temperature to convert: "))
        temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        fahrenheit = temp_input
        if fahrenheit and temp_state == "F":
                temp_celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
                print(f"{fahrenheit}F is {temp_celsius}°C")
        else:
                print("Invalid temperature. Please enter a numeric value.")

    
# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
        temp_input = float(input("Enter the temperature to convert: "))
        temp_state = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        celsius = temp_input
        if celsius and temp_state == "C":
                temp_fahrenheit = (32 + (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR))
                print(f"{celsius}°C is {temp_fahrenheit}F")
        else:
                print("Invalid temperature. Please enter a numeric value.")
        
        


