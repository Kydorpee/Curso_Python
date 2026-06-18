
def somar (x,y):
    soma = x+y
    print(f"A soma dos numero é {soma}")
    return


try: 
    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))
    somar(numero1,numero2)
except ValueError:
    print ("Digite um valor valido!")
    
