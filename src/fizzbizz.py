
def calculate_fizzbuzz(val):
    if (isinstance(val, int)):
        return calc(val)
    else:
        raise ValueError

def calc(val):
    if(isValue_aFizz(val) and isValue_aBuzz(val)):
        return "FizzBuzz"
    elif(isValue_aFizz(val)):
        return "Fizz"
    elif(isValue_aBuzz(val)):
        return "Buzz"
    else:
        return f"{val}"

def isValue_aFizz(val):
    if(val % 3 is 0 and val is not 0):
        return True
    return False

def isValue_aBuzz(val):
    if(val % 5 is 0 and val is not 0):
        return True
    return False