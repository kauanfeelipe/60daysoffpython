import threading
import time

def tarefa(nome,tempo_execucao):
    print(f'Tarefa {nome} iniciada')
    time.sleep(tempo_execucao)
    print(f'Tarefa {nome} finalizada')

threading1 = threading.Thread(target=tarefa, args=('Dowload tarefa 1', 3))
threading2 = threading.Thread(target=tarefa, args=('Dowload tarefa 2', 4))

threading1.start()
threading2.start()

threading1.join()
threading2.join()

print('Todas as tarefas foram finalizadas')

