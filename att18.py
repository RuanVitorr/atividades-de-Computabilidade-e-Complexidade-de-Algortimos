#18 - Desenvolva um AFD que reconheça a linguagem de strings sobre {0, 1} com número ímpar de '0's e '1's.

def afd_impar_zeros_uns(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'  
            elif char == '1':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == '0':
                estado = 'q0'  
            elif char == '1':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '0':
                estado = 'q3' 
            elif char == '1':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q3':
            if char == '0':
                estado = 'q2'  
            elif char == '1':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

    
    if estado == 'q3':
        return "palavra valida (número ímpar de '0's e '1's)"
    else:
        return "palavra invalida (número par de '0's ou '1's)"

# Testes
print(afd_impar_zeros_uns("01"))      # Valida
print(afd_impar_zeros_uns("0011"))    # Invalida
print(afd_impar_zeros_uns("1100"))    # Invalida
print(afd_impar_zeros_uns("101"))     # Valida
print(afd_impar_zeros_uns("000111"))  # Valida
print(afd_impar_zeros_uns("0000"))    # Invalida
