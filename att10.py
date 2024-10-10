#10 - Implemente um AFN que aceite qualquer string que tenha pelo menos um '0' seguido de pelo menos um '1'.

def afn_aceita_zero_seguido_de_um(palavra):
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
                estado = 'q1'
            elif char == '1':
                estado = 'q2'
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q2':
        return "palavra valida (contém pelo menos um '0' seguido de pelo menos um '1')"
    else:
        return "palavra invalida (não contém '0' seguido de '1')"

# Testes
print(afn_aceita_zero_seguido_de_um("01"))        # Valida
print(afn_aceita_zero_seguido_de_um("001"))       # Valida
print(afn_aceita_zero_seguido_de_um("100"))       # Valida
print(afn_aceita_zero_seguido_de_um("111"))       # Invalida
print(afn_aceita_zero_seguido_de_um("0101"))      # Valida
print(afn_aceita_zero_seguido_de_um("000"))       # Invalida
print(afn_aceita_zero_seguido_de_um("1110001"))   # Invalida
print(afn_aceita_zero_seguido_de_um("0001101"))   # Valida
