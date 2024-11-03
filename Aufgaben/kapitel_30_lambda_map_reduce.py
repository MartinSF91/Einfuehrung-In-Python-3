""" Aufgabe 1"""
orders = [
    ["34587", "Learning Python", 4, 40.95],
    ["98762", "Programming Python", 5, 56.8],
    ["77226", "Head First Python", 3, 32.95],
]

invoice_totals = list(
    map(
        lambda x: (x[0], round(x[2]*x[3], 2)), orders
    )
)

print(invoice_totals)