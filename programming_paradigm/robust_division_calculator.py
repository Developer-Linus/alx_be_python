def safe_divide(numerator, denominator):
    
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator != 0:
            return numerator/denominator
        else:
            return "Error: Cannot divide by zero."
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only")