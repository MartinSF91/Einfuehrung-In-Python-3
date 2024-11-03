# print([(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 7])

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [((float(9) / 5) * x + 32) for x in celsius]

print(fahrenheit)