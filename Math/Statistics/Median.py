def Median(Numbers):
    """
    Returns the median of a List

    args:
        Numbers (Int | Float | List): The List of the numbers to return the median of
    """

    def Floor(Float):
        """
        Floor rounds "Float" then returns it

        args:
            Float (float): The float to be floor rounded
        """

        # Try to convert "Float" to a Float just in case it is not already
        try:
            Float = float(Float)

        except:
            raise TypeError(f"Argument \"Float\" must be a float, not {type(Float)}")

        return (int(Float))

    # Check whether the list of numbers is even or odd
    NumbersLength = len(Numbers)
    if (NumbersLength % 2) == 1:
        isOdd = True
    elif (NumbersLength % 2) == 0:
        isOdd = False
    Numbers.sort()

    if isOdd is True:
        middleIndex = NumbersLength / 2

        middleIndex = Floor(middleIndex)
        
        median = Numbers[int(middleIndex)]

        return median

    elif isOdd is False:
        middleIndex = NumbersLength / 2

        middleIndex_HIGH = int(middleIndex)
        middleIndex_LOW = int(middleIndex - 1)

        median = (Numbers[middleIndex_LOW] + Numbers[middleIndex_HIGH]) / 2

        return median
