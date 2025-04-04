from random import randint

def lancar_dado():
    
    return randint(1, 6)

if __name__ == "__main__":
    print(f"O resultado do dado foi: {lancar_dado()}")