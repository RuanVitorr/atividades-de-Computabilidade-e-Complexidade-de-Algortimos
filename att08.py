# 8 - Desenvolva um AFN que aceite strings onde o número de '0's é divisível por 3.
def afn_zeros_divisivel_por_3(palavra):
    estado = 'q0'  # Começa no estado q0

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
                estado = 'q2'
            elif char == '1':
                estado = 'q1'
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '0':
                estado = 'q0'
            elif char == '1':
                estado = 'q2'
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q0':
        return "palavra valida (número de '0's é divisível por 3)"
    else:
        return "palavra invalida (número de '0's não é divisível por 3)"

# Testes
print(afn_zeros_divisivel_por_3("000"))      # Valida
print(afn_zeros_divisivel_por_3("00100"))    # Valida
print(afn_zeros_divisivel_por_3("100010"))   # Valida
print(afn_zeros_divisivel_por_3("01"))       # Invalida
print(afn_zeros_divisivel_por_3("111"))      # Valida (zero '0's é divisível por 3)
print(afn_zeros_divisivel_por_3("0001"))     # Valida
