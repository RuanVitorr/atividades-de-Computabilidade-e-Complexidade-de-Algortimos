#4-Desenvolva um AFD que aceite strings com pelo menos um '0'

def valida_string_com_zero(palavra):
    estado = 'q0'

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'
            elif char == '1':
                estado = 'q0'
            else:
                return 'palavra invalida'
        elif estado == 'q1':
            if char == '0' or char == '1':
                estado = 'q1'
            else:
                return 'palavra invalida'

    if estado == 'q1':
        return "palavra valida (contém pelo menos um '0')"
    else:
        return "palavra invalida (não contém nenhum '0')" 

# Testes
print(valida_string_com_zero("1001"))  # Valida
print(valida_string_com_zero("111"))    # Invalida
print(valida_string_com_zero("001"))    # Valida
print(valida_string_com_zero("010"))    # Valida
print(valida_string_com_zero("1"))      # Invalida
