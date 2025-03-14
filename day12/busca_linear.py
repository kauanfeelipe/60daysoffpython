def busca_linear(lista, numero_procurado):
    for i , numero in enumerate(lista):
        if numero == numero_procurado:
            return i
    return -1

lista = [10,2,4,7,8,11,15,20,25,30,40,50,60,70,80,90,100]
numero_procurado = 7  

buscando = busca_linear(lista, numero_procurado)
print(buscando)    
   
if buscando != -1:
    print(f"O numero {numero_procurado} foi encontrado na posição {buscando}")
else:
    print(f"O numero {numero_procurado} não foi encontrado na lista")
    
        
"""
    Procurar um numero dentro de uma lista utioizando busca linear
    :param lista: lista de numeros
    :param numero_procurado: o numero que procurar
    
    """
    
#enumerate função nativa do python que itera e enquanto contabiliza o indice

    
# for i , numero in enumerate([1,2,3,4,5,6]):
#     print(f"indice: {i} - numero: {numero}")
    
    


