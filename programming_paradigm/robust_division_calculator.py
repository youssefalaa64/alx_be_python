def safe_divide(numerator, denominator) :
    try :
        float_num = float(numerator)
        float_den = float(denominator)
        return f"The result of the division is {float_num / float_den}"
    except ZeroDivisionError :
        return "Error: Cannot divide by zero."
    except ValueError :
        return "Error: Please enter numeric values only."
    except Exception as e :
        return f"unexpected error occured : {e}"