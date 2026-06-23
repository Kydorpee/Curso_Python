frase = ''

def receber_frase(frase):
    frase = input("Digite uma frase: ")
    frase=tratar_frase(frase)
    return frase
def contar_palavras(frase):
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra,0)+1
    return contagem
def tratar_frase(frase):
    frase = frase.lower()
    caracter = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~"

    for char in caracter:
        frase = frase.replace(char,"")
    
    return frase

