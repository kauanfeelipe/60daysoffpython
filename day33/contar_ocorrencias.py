from collections import Counter

def contar_ocorrencias(lista):
    
    contagem = Counter(lista)
    for elemento,quantidade in contagem.itens():
        print(f"{elemento}: {quantidade}")
    
    return "contagem realizada com sucesso!"

if __name__ == "__main__":
    lista_exemplo = ['banana','laranja','uva','laranja','uva','pera']
    
print(Counter(lista_exemplo))