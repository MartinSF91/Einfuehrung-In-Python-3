"""Aufgabe 1"""

# roemische_zahl = str(input("Römische Zahl: "))

"""Aufgabe 2"""
jumps = 10
strecke = 0

for i in range(jumps + 1):
    strecke += 1 / (2**i)
    print(strecke)

print(strecke)
