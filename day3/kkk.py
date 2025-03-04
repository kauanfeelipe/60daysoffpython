# numero = int(input("Digite o numero: "))

# if numero % 2 == 0:
#     print(f"Este numero é par ==> {numero}")
# else:
#     print("Este numero nao é par")
    
    
    
entrada = input("Coloque o numero: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero é impar.")
except ValueError:
    print("Voce nao passou um numero inteiro")
                