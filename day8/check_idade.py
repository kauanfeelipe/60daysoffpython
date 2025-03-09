# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Maior de idade, pode dirigir")
# else:
#     print("Menor de idade, nao pode dirigir")   
    
def check_dirigir(idade):
    if idade >= 18:
        return True 
    else:
        return False
print(check_dirigir(18))


try:
    input_user = int(input("Digite sua idade: "))
    print(check_dirigir(input_user))
    
except ValueError:
    print("Voce nao passou um numero inteiro")
                           