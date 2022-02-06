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
