"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Yehor Baranov
email: yhr.baranov@post.cz

"""
import re
import time
from task_template import TEXTS # import textů
from collections import Counter

separator = '-' * 40 # dělící čára


# Přihlášení uživatelů
users_registred = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz":"pass123"
}

print(separator)

print(f"Sign in:")
name = input("name: ").lower().strip()

# Kontrola, zda je uživatel registrován
if name not in users_registred.keys():
    print(separator)
    print("unregistered user, terminating the program.")
    time.sleep(3) # Zpoždění na 3s před uzavřením programu
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
                print(separator)
                print("Access denied. Terminating the program.")
                time.sleep(3) # Zpoždění na 3s před uzavřením programu
                exit()

print(separator)

print(f"Welcome to the app, {name.capitalize()}")


# Výběr textu k analýze
while True:
    text_quantity = len(TEXTS)
    print(f"We have {text_quantity} texts to be analyzed.")

    print(separator)

    number_text = input(
        f"Enter a number btw. 1 and {text_quantity} to select \n"
        "or <Enter> to exit: "
        )

    print(separator)

    if number_text == "":  # Ukončení programu při stisknutí klávesy Enter
        print("Exiting the program. Goodbye!")
        time.sleep(3) # Zpoždění na 3s před uzavřením programu
        exit()
        break

    # Kontrola zadání čísla textů
    if number_text.isdigit():
        number_text = int(number_text)
        if number_text not in range(1, text_quantity + 1):
            print(
                "The selected text number is not valid. "
                "Terminating the program."
            )
            time.sleep(3) # Zpoždění na 3s před uzavřením programu
            exit()
    else:
        print("The selected is not valid. Terminating the program.")
        time.sleep(3) # Zpoždění na 3s před uzavřením programu
        exit()


    # Analýza textu podle výběru
    text_selected = TEXTS[number_text - 1] # Výběr textu ze seznamu

    # Vyčištění textu od mezer a interpunkčních znamének
    text_list = list(filter(None, re.split(r'\W+', text_selected)))

    # Nalezení a počítání titulních slov
    word_titlecase = sum(1 for word in text_list if word.istitle())

    # Nalezení a počítání slov psaných velkými písmeny
    word_uppercase = sum(1 for word in text_list 
                        if word.isupper() and word.isalpha()
                        )

    # Nalezení a počítání slov psaných malými písmeny
    word_lowercase = sum(1 for word in text_list if word.islower())

    # Nalezení a počítání čísel
    numbers = sum(1 for number in text_list if number.isdigit())
    numbers_sum = 0
    for number in text_list:
        if number.isdigit():
            number = int(number)
            numbers_sum += number

    # Závěr výsledků analýzy textu
    print(f"There are {len(text_list)} words in the selected text.")
    print(f"There are {word_titlecase} titlecase words.")
    print(f"There are {word_uppercase} uppercase words.")
    print(f"There are {word_lowercase} lowercase words.")
    print(f"There are {numbers} numeric strings.")
    print(f"The sum of all the numbers {numbers_sum}")


    # Zjištění délky slov a počtu výskytů v textu
    word_len = Counter(len(word) for word in text_list)

    word_len = dict(sorted(word_len.items()))
    
    # Zobrazení sloupcového grafu
    print(separator)
    # Tisk záhlaví tabulky
    print(f"{'LEN':<4}|{'OCCURENCES':^18}|{'NR.':>4}")

    print(separator)

    # Tisk řádků tabulky
    # Formát řetězce: délka slova, hvězdičky podle počtu schůzek, počet schůzek
    for length, count in word_len.items():
        print(f"{length:<4}|{'*' * count:<18}|{count:>4}")
    
    print(separator)
