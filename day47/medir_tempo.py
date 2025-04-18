import time

def medir_tempo_execucao(funcao):
    """
    Decorador para medir o tempo de execução de uma função.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Captura o tempo de início
        result = funcao(*args, **kwargs)  # Chama a função original
        end_time = time.time()
        # Calcula o tempo total de execução
        total_time = end_time - start_time
        print(f"Tempo de execução: {total_time} ")
        return result
    return wrapper

@medir_tempo_execucao
def tarefa_1():
    print("Rodando a funcao ")
    time.sleep(3)  # Simula uma tarefa que leva 2 segundos
    print("Funcao finalizada")

@medir_tempo_execucao
def tarefa_2():
    print("Rodando a funcao 2 ")
    time.sleep(2)  # Simula uma tarefa que leva 2 segundos
    print("Funcao finalizada")
    
tarefa_1()
tarefa_2()