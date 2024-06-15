"""Aufgabe 1"""
def multiple_3(n):
    # print(f"n: {n}")
    if n == 1:
        return 3
    else:
        res = multiple_3(n-1) + 3
        # print(f"res: {res}")
        return res
    
n = 4
print(multiple_3(n))


"""Aufgabe 2"""
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
n = 100
print(sum(n))