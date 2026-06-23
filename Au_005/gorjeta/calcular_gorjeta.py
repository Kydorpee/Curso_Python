

def fechar_conta():
    try:
        total = float(input("Digite o valor total da conta: "))
        total = round(total,2)

        gorjeta = float(input("Digite a porcentagem de gorjeta que deseja pagar, sugerimos o padrão de 10%: "))
        gorjeta = round(gorjeta,2)

        valo_gorjeta = round(total*(gorjeta/100),2)
        valor_total = round((valo_gorjeta + total),2)
        
        print("--------------------------------------")
        print(f"O valor da sua conta é R${total}")
        print(f"O valor da gorjeta de %{gorjeta} é R${valo_gorjeta}")
        print (f"Seu valor total da conta a ser paga é R${valor_total}")
        print("--------------------------------------")

    except NameError:
        input("Valores invalidos favor tentar novamente!")
        fechar_conta()

fechar_conta()

    



    