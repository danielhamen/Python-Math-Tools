def Degrees(Expression, AsNomial=False):
    """
    Returns the degrees of an expression

    args:
        Expression (str): The expression that will get the degrees of

        AsNomial (bool): When True, instead of a number, the script will return the state as either: Monomial, Binomial, Trinomial, or Polynomial
    """

    Expression = str(Expression)
    Expression = Expression.replace("+", ";").replace("-", ";").replace("/", ";").replace("*", ";").replace("÷", ";")

    ExpressionList = Expression.split(";")
    
    Degrees = len(ExpressionList)

    if AsNomial is True:
        if Degrees < 1:
            return None

        elif Degrees == 1:
            return "Monomial"
        
        elif Degrees == 2:
            return "Binomial"

        elif Degrees == 3:
            return "Trinomial"

        else:
            return "Polynomial"
