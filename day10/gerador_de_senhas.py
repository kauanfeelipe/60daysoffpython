import random
import string

#String fornece um conjunto de caracteres pronto

def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
    print(f"Sua senha gerada foi: {senha}")    

gerador_de_senhas(10) 
