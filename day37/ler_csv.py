import pandas as pd

def main():
    nome_arquivo = 'test.csv'
    
    df = pd.read_csv(nome_arquivo)
    
    ## Exibir as primeiras linhas do DataFrame
    print(df.head())
    
    #pega informações do df
    print(df.info())
    
    #exibe o formato do df
    print(df.shape)
    
if __name__ == '__main__':
    main()
    