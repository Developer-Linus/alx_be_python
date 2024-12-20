# The user is prompted to enter the size of the pattern.
pattern = int(input("Enter the size of the pattern: "))

i = 1
while i <= pattern:
    for j in range(pattern, 0, -1):  # Loop from 'pattern' down to 1
        print('*', end = " ")
    i += 1
    print()  # Print a new line after each row

