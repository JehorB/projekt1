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
name = input("name: ")

# Kontrola, zda je uživatel registrován
if name.lower() not in users_registred.keys():
    print("unregistered user, terminating the program.")
    exit(input("Press <Enter> to exit..."))
# Ověření hesla s možností dalších pokusů
else:
    attempts = 3  # Celkový počet pokusů
    while attempts > 0:
        password = input("password: ")
        if password == users_registred[name.lower()]:
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(
                    f"Incorrect password. You have {attempts} attempt(s) left."
                )
            else:
                print("Access denied. Terminating the program.")
                exit(input("Press <Enter> to exit..."))


# Výběr textu k analýze
