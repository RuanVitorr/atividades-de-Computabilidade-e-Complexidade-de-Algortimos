#22 - Desenvolva um AFD que reconheça uma linguagem onde a diferença entre o número de 'a's e 'b's seja múltipla de 3.

def afd_diferenca_multiplos_de_3(palavra):
    estado = 'q0'  # Estado inicial

    for char in palavra:
        if estado == 'q0':
            if char == 'a':
                estado = 'q1'  
            elif char == 'b':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q1':
            if char == 'a':
                estado = 'q2' 
            elif char == 'b':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q2':
            if char == 'a':
                estado = 'q3'  
            elif char == 'b':
                estado = 'q1' 
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q3':
            if char == 'a':
                estado = 'q4'  
            elif char == 'b':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q4':
            if char == 'a':
                estado = 'q5' 
            elif char == 'b':
                estado = 'q3' 
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q5':
            if char == 'a':
                estado = 'q4'  
            elif char == 'b':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado in ['q0', 'q5']:
        return "palavra valida (diferença entre 'a's e 'b's é múltipla de 3)"
    else:
        return "palavra invalida (diferença entre 'a's e 'b's não é múltipla de 3)"

# Testes
print(afd_diferenca_multiplos_de_3("aaabbb"))    # Valida
print(afd_diferenca_multiplos_de_3("ab"))        # Valida
print(afd_diferenca_multiplos_de_3("aaaabbbb"))  # Invalida
print(afd_diferenca_multiplos_de_3("aabb"))      # Invalida
print(afd_diferenca_multiplos_de_3("aaa"))       # Valida
print(afd_diferenca_multiplos_de_3("bbb"))       # Invalida
print(afd_diferenca_multiplos_de_3("aabab"))     # Valida
print(afd_diferenca_multiplos_de_3("bbaaa"))     # Invalida
print(afd_diferenca_multiplos_de_3("abbaa"))     # Invalida

         
