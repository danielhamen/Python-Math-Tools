# How to use the Degrees() function:
## Steps:
> First import the function:
> ```python
> from Degree import Degrees
> ```
> 
> After importing, you can now use ```Degrees()```. This function has the following arguments:
>> Degrees(<i>Expression</i>, <i>AsNomial</i>)
>> 
>>> <i>Expression</i> (str):
>>> 
>>>> The expression that will get the degrees of (As ```int()```)
>>>> 
>>> <br>
>>> 
>>> <i>AsNomial</i> (bool):
>>> 
>>>> When True, instead of a number, the script will return the state as either: ```Monomial```, ```Binomial```, ```Trinomial```, or ```Polynomial```
> 
> Example:
> ```python
> x = "6xy^2-7+6y/h^4"
> 
> Deg = Degrees(x, True)
> 
> print(Deg)
> 
> >>> Polynomial
> 
> Deg = Degrees(x, False)
> 
> print(Deg)
> 
> >>> 4
> ```
