def fatorial(n):
    if n < 0:
        raise ValueError("Numero não pode ser negativo")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(5)) # 120

try:
    print(f"Fatorial igual a {fatorial(-3)}")
except ValueError as e:
    print(e)