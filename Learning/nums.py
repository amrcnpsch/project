from math import pi
def plus(a: int,b: int) -> int:
    return a+b
def minus(a,b):
    return a-b
def delenie(a,b):
    if b != 0:
        return a/b
    else:
        print("B is a null!")
def umnozhenie(a,b):
    return a*b
def dlina(r):
    return pi*r
print(plus(4,5))