#14 - Crie um AFN que aceite strings binárias onde as substrings "11" e "00" não aparecem

def afn_substrings_proibidas(palavra):
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
                return 'palavra invalida (substring "00" encontrada)'
            elif char == '1':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q2':
            if char == '1':
                return 'palavra invalida (substring "11" encontrada)'
            elif char == '0':
                estado = 'q3'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q3':
            if char == '0':
                estado = 'q1'  
            elif char == '1':
                estado = 'q2'  
            else:
                return 'palavra invalida (caractere inválido)'

    return "palavra valida (não contém substrings '11' ou '00')"

# Testes
print(afn_substrings_proibidas("010"))         # Valida
print(afn_substrings_proibidas("101"))         # Valida
print(afn_substrings_proibidas("000"))         # Invalida
print(afn_substrings_proibidas("111"))         # Invalida
print(afn_substrings_proibidas("0101"))        # Valida
print(afn_substrings_proibidas("001"))         # Invalida
print(afn_substrings_proibidas("1010"))        # Valida
print(afn_substrings_proibidas("1100"))        # Invalida
print(afn_substrings_proibidas("000111"))      # Invalida
