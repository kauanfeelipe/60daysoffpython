def anagrama(palavra1, palavra2):
    """
    Verifica se duas palavras são anagramas.
    Retorna True se forem anagramas e False caso contrário.


    """
    
    
    #removendo espaços e convertendo para minúsculo
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras são anagramas"
    return f"Essas palavras não são anagramas"

print(anagrama("amor", "roma")) # True

    
    