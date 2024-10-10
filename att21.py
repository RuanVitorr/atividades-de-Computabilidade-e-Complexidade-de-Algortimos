#21 - Implemente um AFN que aceite todas as strings sobre {a, b} que tenham um 'a' após cada 'b'.

def afn_a_apos_b(palavra):
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
            if char == 'a':
                estado = 'q0'  
            elif char == 'b':
                estado = 'q4'  
            else:
                return 'palavra invalida (caractere inválido)'

        elif estado == 'q4':
            return 'palavra invalida (não pode haver "b" sem "a")'

    if estado in ['q0', 'q2']:
        return "palavra valida (tem um 'a' após cada 'b')"
    else:
        return "palavra invalida (não atende aos critérios)"

# Testes
print(afn_a_apos_b("a"))          # Valida
print(afn_a_apos_b("ab"))         # Valida
print(afn_a_apos_b("aab"))        # Valida
print(afn_a_apos_b("abb"))        # Invalida
print(afn_a_apos_b("ba"))         # Invalida
print(afn_a_apos_b("aa"))         # Valida
print(afn_a_apos_b("ababa"))      # Valida
print(afn_a_apos_b("aabba"))      # Valida
print(afn_a_apos_b("bb"))         # Invalida
print(afn_a_apos_b("b"))          # Invalida

