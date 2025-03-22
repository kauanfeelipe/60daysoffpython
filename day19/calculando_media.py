def calcular_media(notas):
    media = sum(notas) / len(notas)
    return round(media, 2)

#round arredonda

print(calcular_media([10, 9, 8, 7, 6])) 

