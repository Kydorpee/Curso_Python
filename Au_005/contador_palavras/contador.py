frase = ''

def receber_frase(frase):
    frase = input("Digite uma frase: ")
    return frase
def contar_palavras(frase):
    palavras = frase.split()
    print(len(palavras))
    print(palavras)
def tratar_frase(frase):
    frase = frase.lower()
    caracter = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~"

    for char in caracter:
        frase = frase.replace(char,"")
    
    return frase

