#função pra verificar palindromo

def palindromo(texto):
    """verificar se um numero ou texto é palindromo
    """
    texto = str(texto).replace(" ", "").lower()
    if texto == texto[::-1]:
        return f"{texto} é palindromo"
    return f"{texto} nao é palindromo"

print(palindromo("oi")) # True