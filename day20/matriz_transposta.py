def transpor_matriz(matriz):
    """Função que retorna a transposta de uma matriz
       Substitui colunas horizontais por linhas verticais
    """
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("Matriz deve ser 3x3")
    
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    return transposta

#utilizando iteradores 
matriz =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]    
transposta = []

for i in range(3):
    nova_linha = []
    
    for j in range(3):
        nova_linha.append(matriz[j][i])
   
    # print(nova_linha)
    transposta.append(nova_linha)   
    
for linha in transpor_matriz(matriz):
    print(linha)
   
 