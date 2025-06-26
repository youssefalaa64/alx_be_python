def safe_divide(numerator, denominator) :
    try :
        float_num = float(numerator)
        float_den = float(denominator)
        return float_num / float_den
    except ZeroDivisionError :
        return "you cannot devide by zero"
    except ValueError :
        return "sorry, invalid input"
    except Exception as e :
        return f"unexpected error occured : {e}"