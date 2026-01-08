import random
import string

letters = string.ascii_letters

c = ""
counter = 0  # initialisation du compteur

while c != "w":
    c = random.choice(letters)
    counter += 1
    print(f"La lettre choisie est : {c}")
    print(f"Le nombre de tirages effectués est : {counter}")
