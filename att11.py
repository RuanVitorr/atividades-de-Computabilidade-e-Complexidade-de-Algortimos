#11 - Construa um AFD para uma linguagem sobre o alfabeto {a, b}, que reconheça strings com um número ímpar de 'a's.

def afd_numero_impar_de_as(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == 'a':
                estado = 'q1'  
            elif char == 'b':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == 'a':
                estado = 'q0'  
            elif char == 'b':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q1':
        return "palavra valida (número ímpar de 'a's)"
    else:
        return "palavra invalida (número par de 'a's)"

# Testes
print(afd_numero_impar_de_as("a"))       # Valida
print(afd_numero_impar_de_as("b"))       # Invalida
print(afd_numero_impar_de_as("ab"))      # Valida
print(afd_numero_impar_de_as("aab"))     # Valida
print(afd_numero_impar_de_as("aa"))      # Invalida
print(afd_numero_impar_de_as("bba"))     # Valida
print(afd_numero_impar_de_as("bb"))      # Invalida
print(afd_numero_impar_de_as("aaaa"))    # Invalida
