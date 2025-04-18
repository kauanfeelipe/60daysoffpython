import re   

def validar_email(email):

    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print(f"'{email}' email validado")
    else:
        print(f"'{email}' email invalido")
        
validar_email("kauan@gmail.com")
validar_email("kauan.com")