#20 - Implemente um AFD para strings sobre {a, b} onde a sequência 'ab' aparece exatamente uma vez.

def afd_exato_ab(palavra):
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
                estado = 'q1'  
            elif char == 'b':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q2':
            if char == 'a':
                estado = 'q3' 
            elif char == 'b':
                estado = 'q4' 
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q3':
            if char == 'a':
                estado = 'q3'  
            elif char == 'b':
                estado = 'q4'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q4':
            
            return 'palavra invalida (contém mais de uma sequência "ab")'

    if estado == 'q3':
        return "palavra valida (a sequência 'ab' aparece exatamente uma vez)"
    else:
        return "palavra invalida (não contém a sequência 'ab' exatamente uma vez)"

# Testes
print(afd_exato_ab("ab"))        # Valida
print(afd_exato_ab("abab"))      # Invalida
print(afd_exato_ab("aab"))       # Invalida
print(afd_exato_ab("baab"))      # Valida
print(afd_exato_ab("aaaabbbb"))  # Invalida
print(afd_exato_ab("b"))         # Invalida
print(afd_exato_ab("a"))         # Invalida
print(afd_exato_ab("babab"))     # Valida
print(afd_exato_ab("abaaa"))     # Valida
