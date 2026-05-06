
import  random

contador = 0
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
fruit_salad = random.sample(frutas,3)


usuario = input('Digite seu nome: ')
print(f"Olá {usuario}, sua salada de frutas sera composta por",",".join(fruit_salad))
