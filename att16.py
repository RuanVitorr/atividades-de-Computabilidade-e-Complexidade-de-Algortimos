#16 - Construa um AFD para reconhecer strings sobre {0, 1} onde os '0's aparecem em blocos consecutivos

def afd_blocos_consecutivos(palavra):
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
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q3':
            return 'palavra invalida (caractere inválido)'

    if estado == 'q1' or estado == 'q2':
        return "palavra valida (os '0's aparecem em blocos consecutivos)"
    else:
        return "palavra invalida (os '0's aparecem em blocos não consecutivos)"

# Testes
print(afd_blocos_consecutivos("1"))        # Valida
print(afd_blocos_consecutivos("0"))        # Valida
print(afd_blocos_consecutivos("000"))      # Valida
print(afd_blocos_consecutivos("111"))      # Valida
print(afd_blocos_consecutivos("101"))      # Valida
print(afd_blocos_consecutivos("11011"))    # Valida
print(afd_blocos_consecutivos("1001"))     # Valida
print(afd_blocos_consecutivos("100001"))   # Valida
print(afd_blocos_consecutivos("100010"))   # Invalida
print(afd_blocos_consecutivos("010"))      # Invalida
print(afd_blocos_consecutivos("101010"))    # Invalida
