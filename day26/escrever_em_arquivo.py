def escrever_arquivo(nome_arquivo,conteudo):
    with open(nome_arquivo,"w") as arquivo:
        arquivo.write(conteudo)
        
        print(f"Arquivo {nome_arquivo} criado com sucesso")
        
def ler_arquivo(nome_arquivo):
    
    try:
        with open(nome_arquivo,"r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} nao encontrado")
        
def main(nome_arquivo,conteudo):
    
    print("bem vindo ao nosos programa de escrita e leitura")
    escrever_arquivo(nome_arquivo,conteudo)
    print("Fazendo leitura do arquivo")
    ler_arquivo(nome_arquivo)
    
    
if __name__ == "__main__":
    nome_arquivo = "exemplo.txt"
    texto = "modificando...."
    
    main(nome_arquivo,texto)
            
    