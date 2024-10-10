#9 - Construa um AFD em Python que reconheça strings contendo a sequência "101".

def afd_reconhece_101(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '1':
                estado = 'q1'
            elif char == '0':
                estado = 'q0'
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == '0':
                estado = 'q2'
            elif char == '1':
                estado = 'q1'
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '1':
                estado = 'q3'
            elif char == '0':
                estado = 'q0'
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q3':
            
            if char == '0' or char == '1':
                estado = 'q3'
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q3':
        return "palavra valida (contém a sequência '101')"
    else:
        return "palavra invalida (não contém a sequência '101')"

# Testes
print(afd_reconhece_101("101"))       # Valida
print(afd_reconhece_101("110101"))    # Valida
print(afd_reconhece_101("100"))       # Invalida
print(afd_reconhece_101("010"))       # Invalida
print(afd_reconhece_101("0001"))      # Invalida
print(afd_reconhece_101("11101101"))  # Valida
print(afd_reconhece_101("101010"))    # Valida
