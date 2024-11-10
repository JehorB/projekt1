"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
import re
from task_template import TEXTS # import textů


# stvorení seznamu slov
text_1 = TEXTS[0]
text_2 = TEXTS[1]
text_3 = TEXTS[2]
seznam_slov_1 = list(filter(None, re.split(r'\W+', text_1.lower())))
seznam_slov_2 = list(filter(None, re.split(r'\W+', text_2.lower())))
seznam_slov_3 = list(filter(None, re.split(r'\W+', text_3.lower())))


# Přihlášení uživatelů
users_registred = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz":"pass123"
}

print(f"Sign in:")
name = input("name: ").lower().strip()

# Kontrola, zda je uživatel registrován
if name not in users_registred.keys():
    print("unregistered user, terminating the program.")
    for _ in range(10**8):  # Zpoždění v prázdném cyklu
        pass
    exit()
else: # Ověření hesla s možností dalších pokusů
    attempts = 3  # Celkový počet pokusů
    while attempts > 0:
        password = input("password: ")
        if password == users_registred[name]:
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(
                f"Incorrect password. You have {attempts} attempt(s) left."
                )
            else:
                print("Access denied. Terminating the program.")
                for _ in range(10**8):  # Zpoždění v prázdném cyklu
                    pass
                exit()

print(f"Welcome to the app, {name.capitalize()}")


# Výběr textu k analýze
print("We have 3 texts to be analyzed.")

nomber_text = input("Enter a number btw. 1 and 3 to select: ")

# Kontrola zadání čísla textů
if nomber_text.isdigit():
    if nomber_text not in ("1", "2", "3"):
        print("The selected text number is not valid. Terminating the program.")
        for _ in range(10**8):  # Zpoždění v prázdném cyklu
            pass
        exit()
else:
    print("The selected is not valid. Terminating the program.")
    for _ in range(10**8):  # Zpoždění v prázdném cyklu
        pass
    exit()

input()