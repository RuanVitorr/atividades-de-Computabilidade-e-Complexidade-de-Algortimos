def afn_contem_zero(palavra):
    estados = ['q0']  # Começa no estado q0

    for char in palavra:
        novos_estados = []
        for estado in estados:
            if estado == 'q0':
                if char == '0':
                    novos_estados.append('q1') 
                if char == '1':
                    novos_estados.append('q0')  
            elif estado == 'q1':
                novos_estados.append('q1')  
        estados = novos_estados

    if 'q1' in estados:
        return "palavra aceita (contém pelo menos um '0')"
    else:
        return "palavra rejeitada (não contém '0')"

# Testes
print(afn_contem_zero("1001"))  # Válido
print(afn_contem_zero("111"))   # Inválido
print(afn_contem_zero("001"))   # Válido
print(afn_contem_zero("010"))   # Válido
print(afn_contem_zero("1"))     # Inválido
