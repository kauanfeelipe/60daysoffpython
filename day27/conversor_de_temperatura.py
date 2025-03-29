def celcius_para_fahrenheit(celcius):
    
    
    
    return(celcius * 9/5) + 32

def fahrenheit_para_celcius(fahrenheit):
    
    return round((fahrenheit - 32) * 5/9,2)

def main(temperatura,tipo_conversao):
    if tipo_conversao == "celcius":
        print(celcius_para_fahrenheit(temperatura))
    elif tipo_conversao == "fahrenheit":
        print(fahrenheit_para_celcius(temperatura))
    else:
        return print("Tipo de conversão inválido")
    
if __name__ == "__main__":
    main(20,"celcius")    
    main(20,"fahrenheit")
    