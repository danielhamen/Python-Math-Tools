def Mean(Numbers):
    """
    Returns the Mean (Average) of "Numbers"

    args:
        Numbers (int | float | tuple | list | set | array): The numbers that the mean will be found from
    """

    # Gets the Sum of "Numbers"
    Sum = 0
    for Number in Numbers:
        Sum += float(Number)

    Mean_ = ((Sum) / len(Numbers))

    return Mean_
