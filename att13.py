#13 - Desenvolva um AFD que reconheça strings binárias onde o número de '1's seja maior que o número de '0's.
def afd_numero_maior_de_uns(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '1':
                estado = 'q1'  
            elif char == '0':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == '1':
                estado = 'q1'  
            elif char == '0':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '1':
                estado = 'q1'  
            elif char == '0':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q1':
        return "palavra valida (número de '1's é maior que o número de '0's)"
    else:
        return "palavra invalida (número de '0's é maior ou igual ao número de '1's)"

# Testes
print(afd_numero_maior_de_uns("110"))        # Valida
print(afd_numero_maior_de_uns("1010"))       # Valida
print(afd_numero_maior_de_uns("000"))        # Invalida
print(afd_numero_maior_de_uns("111"))        # Valida
print(afd_numero_maior_de_uns("010"))        # Invalida
print(afd_numero_maior_de_uns("0011"))       # Valida
print(afd_numero_maior_de_uns("0101"))       # Valida
print(afd_numero_maior_de_uns("0000"))       # Invalida
print(afd_numero_maior_de_uns("1"))          # Valida
