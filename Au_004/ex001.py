
atividade_a = int(input("Digite os dias para a atividade A: "))
atividade_b = int(input("Digite os dias para a atividade B: "))
atividade_c = int(input("Digite os dias para a atividade C: "))

total_dias = atividade_a + atividade_b + atividade_c

if total_dias < 0:
    print("Por favor, insira um número inteiro válido para os dias, dias negativos sao invalidos.")
else:
    print(f"O total de dias para as atividades é: {total_dias}")


