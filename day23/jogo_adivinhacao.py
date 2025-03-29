import random
def jogo_adivinhacao():
    
    
    print("Bem vindo ao nosso jogo de adivinhacao")
    
    numero_secreto = random.randint(0,10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite:"))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("Tente um numero maior")
            elif palpite > numero_secreto:
                print("Tente um numero menor")
            else:
                print(f"Parabens, voce acertou o numero secreto em {tentativas} tentativas")
                break
        except ValueError:
            print("Entrada invalida, digite um numero inteiro")

if __name__ == "__main__":
    jogo_adivinhacao()
            