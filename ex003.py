peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

def IMC(X,Y):
    imc = X/Y
    if imc < 18.5:
        print("Voce esta abaixo do peso")
    elif imc < 25:
        print ("Voce esta no peso ideal")
    else:
        print(f"Você esta com sobrepeso, sua pontuação é {imc:2f}")
IMC(peso,altura)