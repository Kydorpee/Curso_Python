
atividade_a = int(input("Digite os dias para a atividade A: "))
atividade_b = int(input("Digite os dias para a atividade B: "))
atividade_c = int(input("Digite os dias para a atividade C: "))
if atividade_a >= 0 and atividade_b >= 0 and atividade_c >= 0:
   
   total_dias = atividade_a + atividade_b + atividade_c
   print("O total de dias para concluir as atividades é:", total_dias)
else:   
    print("Por favor, insira um número válido de dias para cada atividade.")





