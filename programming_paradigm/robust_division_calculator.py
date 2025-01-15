def safe_divide(numerator, denominator):
    
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator != 0:
            result = numerator/denominator
            return f"The result of the division is {result:.1f}"
        else:
            return "Error: Cannot divide by zero."
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        return "Error: Please enter numeric values only."