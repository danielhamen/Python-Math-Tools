def isOdd(Value):
    """
    Checks whether "Value" is odd

    args:
        Value (int): The value that will be checked
    """

    Value = int(Value)

    isOdd = False

    # Check if "Value" is Odd
    if (Value % 2) == 1:
        isOdd = True

    else:
        isOdd = False
    
    return isOdd
