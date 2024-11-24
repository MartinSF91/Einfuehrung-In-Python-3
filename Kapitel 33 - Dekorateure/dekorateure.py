"""
- Funktions- oder Klassendekorateure
- Referenz einer Funktione oder Klasse wird an den Dekorateur übergeben
- Dekorateur liefert modifizierte Funktion der oder Klasse zurück
- Das zu modifizierende Objekt wird dem Dekorateur als Argument übergeben
- Dekorateur liefert modifiziertes Objekt zurück
"""

"""Beispiel 1"""
def our_decorateur(func):
    def function_wrapper(x):
        print(f"Vor dem Aufruf von {func.__name__}")
        func(x)
        print(f"Nach dem Aufruf von {func.__name__}")
        
    return function_wrapper

@our_decorateur
def foo(x):
    print(f"foo wurde mit {str(x)} aufgerufen!")
        
# foo("first")
# foo("second")


"""Beispiel 2"""
from random import random, randint, choice

def decorateur(func):
    def function_wrapper(*args, **kwargs):
        print(f"Vor dem Aufruf von {func.__name__}")
        res = func(*args, **kwargs)
        print(res)
        print(f"Nach dem Aufruf von {func.__name__}")
        
    return function_wrapper

random = decorateur(random)
randint = decorateur(randint)
choice = decorateur(choice)

random()
randint(3, 8)
choice([4, 5, 6])