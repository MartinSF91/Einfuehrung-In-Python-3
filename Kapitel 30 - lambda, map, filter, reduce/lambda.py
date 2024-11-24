
def anwenden(func, accu):
    """
    anwenden erwartet als erstes Argument eine Funktion und als zweites eine Liste.
    anwenden wendet auf jedes Element der übergebenen Liste die als erstes Argument
    übergebenen Funktion an. 
    """
    res = []
    for el in accu:
        res.append(func(el))
    
    return res

print(anwenden(lambda x: x + 42, range(10)))

# Oder kürzer
res = list(map(lambda x: x + 42, range(10)))
print(res)