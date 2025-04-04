import json
from typing import Any

def salvar_dados(arquivo:str, dados: Any) -> None:
    """Salva os dados em um arquivo JSON."""
    with open(arquivo, 'w',encoding='utf-8') as f:
        json.dump(dados,f, indent=4,ensure_ascii=False)
        
def carregar_dados(arquivo:str) -> Any:
    """Carrega os dados de um arquivo JSON."""
    try:
        with open(arquivo, 'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return {}
    
dados_exemplos = {"nome": "Kauan", "cidade": "SP", "cargo": "programador"}

nome_arquivo = "nome_kauan.json"

salvar_dados(nome_arquivo, dados_exemplos)
dados_carregados = carregar_dados(nome_arquivo)
print("Dados carregados:", dados_carregados)
