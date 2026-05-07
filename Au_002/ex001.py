
notas = {'19 Trimestre': 9.5, '2° Trimestre': 9.5, '3º trimestre': 7}

somatorio = sum(notas.values())
qtd_notas = len(notas)


def media(value1, value2):
    media_aluno = value1 / value2
    media_aluno = round(media_aluno, 2)
    print(f"A media do aluno é {media_aluno}!")
    
media(somatorio, qtd_notas)

