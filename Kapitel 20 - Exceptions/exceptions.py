while True:
    try:
        zahl = int(input("Zahl: "))
        break
    except ValueError as e:
        print(f"error message: {e}") 
        print("Error - Keine Zahl!")
        