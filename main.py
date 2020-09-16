def add(num1, num2):
    return int(num1) + int(num2)

def sub(num1, num2):
    return int(num1) - int(num2)

def div(num1, num2):
    return int(num1) / int(num2)

def mult(num1, num2):
    return int(num1) * int(num2)

def opDict(arr):
    return {
        '+' : add(arr[0], arr[2]),
        '-' : sub(arr[0], arr[2]),
        '/' : div(arr[0], arr[2]),
        '*' : mult(arr[0], arr[2])
    }.get(arr[1],"Not a valid basic operator! Please use '+' and '-' for addition and subtraction, and '*' and ' /' for multiplication and division")

def operation(inString):
    opArray = inString.split()
    if(len(opArray) < 3):
        return "Oops, it looks like you didn't use a space somewhere. Try again!\n"
    elif(len(opArray) > 3):
        return "Oops. This calculator only supports two number operations"
    result = opDict(opArray)
    return result
    
def test():
    assert operation("3 + 3") == 6, "Adding isn't working"
    assert operation("3 - 3") == 0, "Subtracting isn't working"
    assert operation("3 * 3") == 9, "Multiplying isn't working"
    assert operation("3 / 3") == 1, "Dividing isn't working"
    
def main():
    print("\nWelcome to the calcuator! Please use a space between your all numbers and operators!\nUse '^^' to exit\n")
    while (True):
        inString = input("Math Expression: ")
        if(inString == '^^'):
            print("\nThank you!\n")
            print("Exiting...")
            break
        result = operation(inString)
        if(isinstance(result, int)):
            print("Result:          "+str(result))
        else:
            print(result)

test()
main()