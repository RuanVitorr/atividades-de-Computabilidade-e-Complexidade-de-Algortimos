#24 - Implemente um AFD que aceite strings sobre {0, 1} onde a sequência "010" aparece pelo menos duas vezes.

def afd_sequencia_010_duas_vezes(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q0'  
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
        return "palavra valida (contém '010' pelo menos duas vezes)"
    else:
        return "palavra invalida (não contém '010' pelo menos duas vezes)"

# Testes
print(afd_sequencia_010_duas_vezes("010010"))  # Valida
print(afd_sequencia_010_duas_vezes("1010"))    # Invalida
print(afd_sequencia_010_duas_vezes("0101010"))  # Valida
print(afd_sequencia_010_duas_vezes("000"))      # Invalida
print(afd_sequencia_010_duas_vezes("110"))      # Invalida
print(afd_sequencia_010_duas_vezes("010101"))    # Valida
print(afd_sequencia_010_duas_vezes("01000100"))  # Valida
print(afd_sequencia_010_duas_vezes("010"))       # Invalida
