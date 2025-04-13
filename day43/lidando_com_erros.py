def dividir(numerador, denominador):
    try:
        
        resultado = numerador / denominador
        print(f"Resultado da divisao é : {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except TypeError:
        print("Erro: Tipo de dado inválido. Verifique se os valores são numéricos.")
    print("função Funcionou corretamente")    
if __name__ == "__main__":
    dividir(5,"e")