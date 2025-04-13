class Ninja:
    def __init__(self,nome,chakra):
        self.nome = nome
        self.chakra = chakra
        
    def usar_jutsu(self,custo_chakra):
        try:
            if custo_chakra > self.chakra:
                raise ValueError("Chakra insuficiente")
            self.chakra -= custo_chakra
            print(f"{self.nome} usou um jutsu com sucesso")
        except ValueError as Error:
            print(f"Erro: {Error} foi detectado. O {self.nome} precisa recuperar seu chakra")
            
            
if __name__ == "__main__":
    naruto = Ninja(nome="Kakashi",chakra= 200)
    naruto.usar_jutsu(300)


