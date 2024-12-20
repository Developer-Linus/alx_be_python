# Prompting the user to enter a number to be used for the multiplication table
number = int(input("Enter a number to see its multiplication table:"))

# for loop for generating the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
# The user is prompted to enter a number, and the multiplication table of the number is displayed.