
notas = {'19 Trimestre': 9.5, '2° Trimestre': 9.5, '3º trimestre': 7}

somatorio = sum(notas.values())
qtd_notas = len(notas)

media = somatorio/qtd_notas
media = round(media,2)

print(f"A media é {media}!")