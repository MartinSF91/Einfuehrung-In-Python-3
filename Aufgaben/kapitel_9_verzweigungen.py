"""Aufgabe 1"""

# hundealter = int(input("Wie alt ist der Hund? "))
# print(f"Hundealter: {hundealter}")

# if hundealter == 1:
#     print("Entspricht einem 14-jährigen Menschen.")
# elif hundealter == 2:
#     print("Entspricht 22 Jahre eines Menschen.")
# else:
#     print(f"Entspricht {22 + (hundealter - 2) * 5} Menschenjahren.")


"""Aufgabe 3"""
sekunden = int(input("Sekunden: "))
minuten = int(input("Minuten: "))
stunden = int(input("Stunden: "))

if sekunden >= 59:
    sekunden = 0
    if minuten == 59:
        minuten = 0
        if stunden == 23:
            stunden = 0
        else:
            stunden += 1
    else:
        minuten += 1
else:
    sekunden += 1


print(f"{stunden}:{minuten}:{sekunden}")
