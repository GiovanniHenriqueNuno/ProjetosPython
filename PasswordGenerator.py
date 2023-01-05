"""
Como criar um gerador de senhas:

1 - É necessário saber a quantidade de caracteres que a senha terá
2 - Quantas senhas serão geradas
3 - Atribuir diversos caracteres e números a uma string
4 - Mostrar as senhas geradas
"""

import random

number = int(input("How many passwords?"))
#Caracteres que podem estar na senha:
characters = 'abcdefghijklmnopqrstuvwxwz123456789-+'
length = int(input("How many characters the password will have?"))


for password in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)
