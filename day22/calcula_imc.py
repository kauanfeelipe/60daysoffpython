def calcula_imc():
    
    
    try:
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        if peso < 0 or altura < 0:
            print("Entrada inválida, digite um numero positivo")
            return
        
        imc = round(peso / (altura ** 2), 2)
        
        if imc < 18.5:
            print(f"Seu IMC é {imc}, abaixo do peso")
            
        elif 18.5 <= imc <= 24.9:
            print(f"Seu IMC é {imc}, peso normal")
            
        elif 25 <= imc <= 29.9:
            print(f"Seu IMC é {imc}, sobrepeso")
        else:
            print(f"Seu IMC é {imc}, obesidade")
            
    except ValueError:
        print("Entrada inválida, digite um numero positivo")
                    
if __name__ == "__main__":
    calcula_imc()
        