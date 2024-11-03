# Beispiel 1
temp = (36.5, 37, 37.5, 39)

F_liste = list(map(lambda C: (5 / 9) * (C - 32), temp))
C_liste = list(map(lambda F: (9 / 5) * F + 35, F_liste))

# print(F_liste)
# print(C_liste)

# Beispiel 2
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y: x + y, a, b)))
print(list(map(lambda x, y, z: x + y + z, a, b, c)))