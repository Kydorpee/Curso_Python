frase = ''

def receber_frase(x):
    x = input("Digite uma frase: ")
    return x
def contar_palavras(x):
    palavras = x.split()
    print(len(palavras))
    print(palavras)

frase = receber_frase(frase)
contar_palavras(frase)