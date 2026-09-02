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

def acha_erro(passw:str) -> None:
    for caracter in passw:
        if caracter not in maiusculas and caracter not in minusculas and caracter not in numeros and caracter not in especiais:
            print("Senha contém caracteres inválidos!!")
            sys.exit()

acha_erro(senha)
if len(senha) == 0:
    print('Senha Vazia!')
elif len(senha) >= 12 and acha_letras(senha, maiusculas) >= 3 and acha_letras(senha, minusculas) >= 3 and acha_letras(senha, numeros) >= 3 and acha_letras(senha, especiais) >= 3:
    print('Senha Muito Forte!')
elif len(senha) >= 9 and acha_letras(senha, maiusculas) >= 2 and acha_letras(senha, minusculas) >= 2 and acha_letras(senha, numeros) >= 2 and acha_letras(senha, especiais) >= 2:
    print('Senha Forte!')
elif len(senha) < 7 or acha_letras(senha, maiusculas) < 1 or acha_letras(senha, minusculas) < 1 or acha_letras(senha, numeros) < 1 or acha_letras(senha, especiais) < 1:
    print('Senha Fraca!') 
elif len(senha) < 9 or acha_letras(senha, maiusculas) < 2 or acha_letras(senha, minusculas) < 2 or acha_letras(senha, numeros) < 2 or acha_letras(senha, especiais) < 2:
    print('Senha Média!')



