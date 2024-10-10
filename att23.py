#23 - Construa um AFN que aceite qualquer string que contenha a sequência "101" ou "110" sobre {0, 1}

def afn_sequencia_101_ou_110(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q0'  
            elif char == '1':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q1':
            if char == '0':
                estado = 'q2'  
            elif char == '1':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q2':
            if char == '0':
                estado = 'q0' 
            elif char == '1':
                estado = 'q4'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q3':
            if char == '0':
                estado = 'q0'  
            elif char == '1':
                estado = 'q5'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q4' or estado == 'q5':  
            if char == '0':
                estado = 'q0'  
            elif char == '1':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

    
    if estado in ['q4', 'q5']:
        return "palavra valida (contém '101' ou '110')"
    else:
        return "palavra invalida (não contém '101' ou '110')"

# Testes
print(afn_sequencia_101_ou_110("10101"))   # Valida
print(afn_sequencia_101_ou_110("110"))     # Valida
print(afn_sequencia_101_ou_110("001"))     # Invalida
print(afn_sequencia_101_ou_110("111"))     # Invalida
print(afn_sequencia_101_ou_110("010101"))   # Valida
print(afn_sequencia_101_ou_110("111010"))   # Valida
print(afn_sequencia_101_ou_110("000"))     # Invalida
print(afn_sequencia_101_ou_110("1001"))    # Valida
