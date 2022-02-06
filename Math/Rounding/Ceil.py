def Ceil(Float):
    """
    Ceiling rounds "Float" then returns it

    args:
        Float (float): The float to be ceiling rounded
    """

    # Try to convert "Float" to a Float just in case it is not already
    try:
        Float = float(Float)
    
    except:
        raise TypeError(f"Argument \"Float\" must be a float, not {type(Float)}")

    return (int(Float) + 1)
