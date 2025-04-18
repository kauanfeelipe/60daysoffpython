
def numeros_inifinito():
    num = 0
    while True:
        yield num
        num += 1

gerador = numeros_inifinito()
for _ in range(10001):
    print(next(gerador))
    