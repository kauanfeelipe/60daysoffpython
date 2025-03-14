def contadorPersonalizdo():
    try:
        limite = int(input("Digite o valor maximo do contador: "))
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("Entrada invalida, digite um numero inteiro")
        
contadorPersonalizdo()
            
