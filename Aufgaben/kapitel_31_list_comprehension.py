"""Aufgabe 2"""
is_seven = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 7]
is_not_seven = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y != 7]

print(f"{round((len(is_seven) / (len(is_seven) + len(is_not_seven))) * 100, 2)}%")


"""Aufgabe 3"""
proba = []
for i in range(1, 13):
    is_sum = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == i]
    is_not_sum = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y != i]
    proba.append(round(((len(is_sum) / (len(is_sum) + len(is_not_sum)))) * 100, 2))

print(proba)
