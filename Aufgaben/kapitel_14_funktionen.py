"""Aufgabe 1"""
# def text_to_loeffelsprache(eingabe):
    
#     mapping = {
#         "diphtong": {
#             "ei": "eilewei",
#             "au": "aulewau",
#             "ie": "ielewie",
#             "eu": "euleweu",
#             },
#         "einzel": {
#             "e": "elewe",
#             "a": "alewa",
#             "i": "ilewi",
#             "o": "olewo",
#             "u": "ulewu",
#             "ä": "älewä",
#             "ö": "ölewö",
#             "ü": "ülewü",
#         }  
#     }
    
#     for i in mapping["diphtong"].keys():
#         eingabe = eingabe.replace(i, mapping["diphtong"][i])
#     for i in mapping["einzel"].keys():
#         eingabe = eingabe.replace(i, mapping["einzel"][i])
#     return eingabe

# eingabe = str(input("Eingabe: "))

# eingabe = eingabe.lower()

# print(text_to_loeffelsprache(eingabe))

"""Aufgabe 3"""
# def is_palindrome(eingabe):
#     eingabe_liste = list(eingabe)
#     eingabe_liste_rev = eingabe_liste.copy()
#     eingabe_liste_rev.reverse()
    
#     return eingabe_liste == eingabe_liste_rev

# eingabe = str(input("Eingabe: "))
# eingabe = eingabe.lower()

# print(is_palindrome(eingabe))

"""Aufgabe 4"""
def is_palindrome(eingabe):
    
    eingabe = list(eingabe
                   .lower()
                   .replace(",", "")
                   .replace(" ", "")
                )
    
    eingabe_rev = eingabe.copy()
    eingabe_rev.reverse()
    
    return eingabe == eingabe_rev

eingabe = str(input("Eingabe: "))

print(f"Eingabe ist ein Palindrom: {is_palindrome(eingabe)}")
