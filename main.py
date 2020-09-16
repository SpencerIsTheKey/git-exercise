def opDict(arr):
    return {
    }.get(arr[1],"Not a valid operator!")

def operation(inString):
    opArray = inString.split()
    if(len(opArray) < 3):
        return "Oops, it looks like you didn't use a space somewhere. Try again!\n"
    elif(len(opArray) > 3):
        return "Oops. This calculator only supports two number operations"
    result = opDict(opArray)
    return result
    
def test():
    
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
            print("Result:          "+result)
        else:
            print(result)

test()
main()