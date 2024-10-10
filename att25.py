#25 - Crie um AFN que reconheça strings sobre {a, b} onde todas as ocorrências de 'a' aparecem antes de todas as ocorrências de 'b'.


def afn_a_antes_b(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == 'a':
                estado = 'q0' 
            elif char == 'b':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q1':
            if char == 'b':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado in ['q1', 'q0']: 
        return "palavra valida (todas as 'a's aparecem antes das 'b's)"
    else:
        return "palavra invalida (não atende aos critérios)"

# Testes
print(afn_a_antes_b("aaabbb"))   # Valida
print(afn_a_antes_b("aab"))      # Valida
print(afn_a_antes_b("aaa"))      # Valida
print(afn_a_antes_b("bbbaaa"))   # Invalida
print(afn_a_antes_b("aabbb"))    # Valida
print(afn_a_antes_b("abab"))     # Invalida
print(afn_a_antes_b("ab"))       # Valida
print(afn_a_antes_b(""))          # Valida (considera como string vazia)
