from functools import reduce

"""
reduce(func, seq) wendet die Funktion func() fortlaufend auf 
eine Sequenz seq an und liefert einen einzelnen Wert zurück.
"""

# Beispiel 1:
print(reduce(lambda x, y: x + y, [47, 11, 42, 13]))


# Beispiel 2:
def add1(res):
    return res + 1

def add2(res):
    return res + 2

res = 1
print(reduce(lambda accu, func: func(accu), [add1, add2], res))