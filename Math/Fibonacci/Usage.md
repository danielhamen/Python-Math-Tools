# Fibonacci
## Follow the steps below to be able to use this script:
> Copy and Paste the "Fibonacci.py" file from this repository to the same directory of your Python project. Then, in your Main Python file, type the following code:
> ```python
> from Fibonacci import Fibonacci
> ```
> <br>
> 
> Now that you have imported the Fibonacci class, you can easily instance it, and use it. To use it, you must create an instance of it and then assign it to a variable:
> ```python
> Fib = Fibonacci(5)
> Fib.Start()
> ```
> <br>
> 
> If you want to print() the Fibonacci sequence, you must do the following: 
> ```python
> print(Fib)
> 
> # Output: 
> >>> ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34', '55']
> ```
> <br>
> The class "Fibonacci" has the following argument:
> 
> ```python
> Fibonacci(AMOUNT_OF_RETURN_NUMBERS)
> ```
> <br>
> 
> The argument above is, as it says- the amount of numbers the script will return. If you would like the return list not to be in a list format, do the following:
> <br>
> 
> ```python
> Fib = ", ".join(Fib)
> ```
> <br>
> 
> The string before ".join(Fib)" is the seperation string in between each string in the list. If that sounds confusing, do not worry as it's not! To explain it better, this is what would happen if you print() the "Fib" variable:
> <br>
> 
> ```python
> Fib = ", ".join(Fib)
> 
> print(Fib)
> 
> # Output:
> >>> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
> ```
> 
> <br>
> If you would like to print() more than 5 sequence numbers, no problem! Just replace the "5" in ```Fibonacci(5)```, with the amount of numbers you would like to print()
> 
> <br>
> 
> ### Final code:
> ```python
> from Fibonacci import Fibonacci
> 
> FibonacciSequence = Fibonacci(25)
> FibonacciSequence = FibonacciSequence.Start()
> 
> FibonacciSequence = ", ".join(FibonacciSequence)
> 
> print(FibonacciSequence)
> >>> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025
> ```
