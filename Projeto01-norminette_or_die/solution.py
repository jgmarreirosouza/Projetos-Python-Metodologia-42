import sys

args = sys.argv
if len(args) <= 1:
    print('Argumentos Insuficientes!')
    sys.exit()
senha = args[1]

maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
             '|', ';', ':', '"', "'", ',', '.', '<', '>', '/', '?', '~', '`']

def acha_letras(passw: str, lista_caracteres: list) -> int: 
    contador_letras = 0
    for caracter in passw:
        if caracter in lista_caracteres:
            contador_letras += 1
    return(contador_letras)

print(acha_letras(senha, maiusculas))
'''
def acha_maiusculas(passw):
    contador_maiusculas = 0
    for caracter in passw:
        if caracter in maiusculas:
            contador_maiusculas += 1
    return(contador_maiusculas)

def acha_minusculas(passw):
    contador_minusculas = 0
    for caracter in passw:
        if caracter in minusculas:
            contador_minusculas += 1
    return(contador_minusculas)

def acha_numeros(passw):
    contador_numeros = 0
    for caracter in passw:
        if caracter in numeros:
            contador_numeros += 1
    return(contador_numeros)

def acha_especiais(passw):
    contador_especiais = 0
    for caracter in passw:
        if caracter in especiais:
            contador_especiais += 1
    return(contador_especiais)

def acha_erro(passw):
    for caracter in passw:
        if caracter not in maiusculas and caracter not in minusculas and caracter not in numeros and caracter not in especiais:
            print("Senha contém caracteres inválidos!!")
            sys.exit()

acha_erro(senha)
if len(senha) == 0:
    print('Senha Vazia!')
elif len(senha) >= 12 and acha_maiusculas(senha) >= 3 and acha_minusculas(senha) >= 3 and acha_numeros(senha) >= 3 and acha_especiais(senha) >= 3:
    print('Senha Muito Forte!')
elif len(senha) >= 9 and acha_maiusculas(senha) >= 2 and acha_minusculas(senha) >= 2 and acha_numeros(senha) >= 2 and acha_especiais(senha) >= 2:
    print('Senha Forte!')
elif len(senha) < 7 or acha_maiusculas(senha) < 1 or acha_minusculas(senha) < 1 or acha_numeros(senha) < 1 or acha_especiais(senha) < 1:
    print('Senha Fraca!') 
elif len(senha) < 9 or acha_maiusculas(senha) < 2 or acha_minusculas(senha) < 2 or acha_numeros(senha) < 2 or acha_especiais(senha) < 2:
    print('Senha Média!')
'''


