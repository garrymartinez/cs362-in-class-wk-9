import pytest

def fibonnaci(num):
    if num <= 1:
        return num
    else:
        return(fibonnaci(num - 1)+fibonnaci(num - 2))

def factorial(num):
    if (num <= 1):
        return 1
    else:
        return (num * factorial(num - 1))
