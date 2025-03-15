numero = int(input("Digite um numero: "))

eh_primo = True

if numero <= 1:
    eh_primo = False

for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        eh_primo = False
        break
    
if eh_primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")