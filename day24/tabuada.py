def tabuada():
    """retorna a tabuada
    """
    try:
        numero = int(input("Digite um numero: "))
        
        print(f"Tabuada do {numero}")
        for i in range(1,11):
            resultado = i * numero
            print(f"{i} x {numero} = {resultado}")
    except ValueError:
        print("Entrada invalida, digite um numero inteiro")
        
        
if __name__ == "__main__":
    tabuada()        