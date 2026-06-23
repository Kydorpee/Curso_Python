from contador import *

frase = receber_frase(frase)
if not frase:
    print("Erro ao indentificar sua frase! tente novamente...")
    input("")
    frase = receber_frase(frase)
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de palavras:")
        for palavra,quantidade in resultado.items():
             print(f"{palavra}:{quantidade}")
        else:
            print("Nenhuma palavra foi localizada!")