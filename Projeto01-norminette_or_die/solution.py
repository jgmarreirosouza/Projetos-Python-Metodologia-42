senha = '527674JgHiiJkkLL@!'
maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
             '|', ';', ':', '"', "'", ',', '.', '<', '>', '/', '?', '~', '`']

def acha_maiusculas(passw):
    contador_maiusculas = 0
    for caracter in passw:
        if caracter in maiusculas:
            contador_maiusculas += 1
    return(contador_maiusculas)
resultado = acha_maiusculas(senha)
print(senha)
print(resultado)