#19 - Construa um AFN que reconheça a linguagem de todas as strings binárias que contenham a substring '010'.

def afn_substring_010(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'  
            elif char == '1':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == '0':
                estado = 'q1'  
            elif char == '1':
                estado = 'q2'  
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
                estado = 'q3'  
            elif char == '1':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q3':
        return "palavra valida (contém a substring '010')"
    else:
        return "palavra invalida (não contém a substring '010')"

# Testes
print(afn_substring_010("010"))       # Valida
print(afn_substring_010("1010"))      # Valida
print(afn_substring_010("001010"))    # Valida
print(afn_substring_010("1001"))      # Invalida
print(afn_substring_010("111"))       # Invalida
print(afn_substring_010("111001"))    # Valida
print(afn_substring_010("00101"))     # Valida
