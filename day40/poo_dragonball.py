class personagemDB:
    def __init__(self, nome, poder,nivel,tranformacao ="base"):
        self.nome = nome
        self.poder = poder
        self.nivel = nivel
        self.tranformacao = tranformacao
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Nível: {self.nivel}")
        print(f"Transformação: {self.tranformacao}")
    
    def treinar(self, horas):
        aumento = horas *10
        self.poder += aumento
        print(f"{self.nome} treinou por {horas} horas e aumentou seu poder em {aumento}.")
        
    def transformar(self, nova_transformacao):
        self.tranformacao = nova_transformacao
        print(f"{self.nome} se transformou em {nova_transformacao}.") 
        
goku = personagemDB(nome="Goku",poder= 9000,nivel="Super Saiyajin")
goku.exibir_informacoes()

vegeta = personagemDB(nome="Vegeta",poder= 8500,nivel="Saiyajin")
vegeta.treinar(horas=10)
vegeta.transformar(nova_transformacao="Super Saiyajin 2")

vegeta.exibir_informacoes()
        
