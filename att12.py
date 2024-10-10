#12 - Implemente um AFN que reconheça strings binárias contendo a substring '110'.

def afn_reconhece_substring_110(palavra):
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
            if char == '1':
                estado = 'q2'  
            elif char == '0':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '0':
                estado = 'q3'  
            elif char == '1':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q3':
            if char == '0' or char == '1':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q3':
        return "palavra valida (contém a substring '110')"
    else:
        return "palavra invalida (não contém a substring '110')"

# Testes
print(afn_reconhece_substring_110("110"))          # Valida
print(afn_reconhece_substring_110("00110"))        # Valida
print(afn_reconhece_substring_110("1001"))         # Invalida
print(afn_reconhece_substring_110("111001"))       # Valida
print(afn_reconhece_substring_110("000"))          # Invalida
print(afn_reconhece_substring_110("011011"))       # Valida
print(afn_reconhece_substring_110("10101"))        # Valida
print(afn_reconhece_substring_110("0001100"))      # Valida
print(afn_reconhece_substring_110("001"))          # Invalida
