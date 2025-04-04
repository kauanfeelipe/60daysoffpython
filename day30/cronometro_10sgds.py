import time

def cronometro_10sgds():
    
    print("Iniciando cronometro....")
    
    tempo = 10
    while tempo > 0:
        print(f"Tempo restante: {tempo} segundos", end="\r", flush=True)
        time.sleep(1)
        tempo -= 1
    print("\nCronometro finalizado!")
    
if __name__ == "__main__":
    cronometro_10sgds()        
        