#5 - Implemente em Python um AFD que aceite qualquer string binária que comece e termine com o mesmo caractere.
def valida_string_binaria(palavra):
    if not palavra:
        return 'palavra invalida (vazia)'

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
                estado = 'q1'
            elif char == '1':
                estado = 'q3'
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q2':
            if char == '1':
                estado = 'q2'
            elif char == '0':
                estado = 'q3'
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q3':
            if char == '0' or char == '1':
                estado = 'q3'
            else:
                return 'palavra invalida (caractere inválido)'

    if estado in ['q1', 'q2', 'q3']:
        return "palavra valida (começa e termina com o mesmo caractere)"
    else:
        return "palavra invalida (não atende aos critérios)"

# Testes
print(valida_string_binaria("0"))      # Válida
print(valida_string_binaria("1"))      # Válida
print(valida_string_binaria("00"))     # Válida
print(valida_string_binaria("11"))     # Válida
print(valida_string_binaria("010"))    # Válida
print(valida_string_binaria("101"))    # Válida
print(valida_string_binaria("100"))    # Inválida
print(valida_string_binaria("0110"))   # Inválida
print(valida_string_binaria("1110"))   # Inválida
