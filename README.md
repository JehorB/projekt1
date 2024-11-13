# Textový analyzátor
**První projekt do Engeto Online Python Akademie**

## Cíl
Cílem tohoto projektu je vytvořit ***textový analyzátor*** - program, který se bude umět 
prokousat libovolně dlouhým textem a zjistit o něm různé informace.

## Co tento program dokáže
- Ověřit uživatele pomocí přihlašovacího jména a hesla
- Nechá uživatele vybrat mezi třemi texty
- Pro vybraný text spočítá následující statistiky:
  - počet slov
  - počet slov začínajících velkým písmenem
  - počet slov psaných velkými písmeny
  - počet slov psaných malými písmeny
  - počet čísel (ne cifer)
  - sumu všech čísel (ne cifer) v textu

## Omezení a varování
- Pokud uživatel je registrovaný, program umožni mu analyzovat texty
    ----------------------------------------
    Sign in:
    name: bob
    password: 123
    ----------------------------------------
    Welcome to the app, Bob
    We have 3 texts to be analyzed.
    ----------------------------------------
    Enter a number btw. 1 and 3 to select
    or <Enter> to exit:

- Pokud není registrovaný, program upozorni jej a skončí

- Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí

- Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí

### Autor
* [Yehor Baranov](https://github.com/JehorB)