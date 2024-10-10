# 7 - Implemente um AFN que reconheça strings que comecem com '01' e terminem com '10'
def afn_comeca_01_termina_10(palavra):
    estados = frozenset(['q0'])  # Começa no estado q0

    for char in palavra:
        novos_estados = set()
        for estado in estados:
            if estado == 'q0':
                if char == '0':
                    novos_estados.add('q1')  
            elif estado == 'q1':
                if char == '1':
                    novos_estados.add('q2')  
            elif estado == 'q2':
                novos_estados.add('q2')  
                if char == '1':
                    novos_estados.add('q3')  
            elif estado == 'q3':
                if char == '1':
                    novos_estados.add('q4')  
            elif estado == 'q4':
                if char == '0':
                    novos_estados.add('q5')  
        estados = frozenset(novos_estados)

    if 'q5' in estados:
        return "palavra valida (começa com '01' e termina com '10')"
    else:
        return "palavra invalida (não atende aos critérios)"

# Testes
print(afn_comeca_01_termina_10("0110"))    # Valida
print(afn_comeca_01_termina_10("01110"))   # Valida
print(afn_comeca_01_termina_10("010"))     # Invalida
print(afn_comeca_01_termina_10("11010"))   # Invalida
print(afn_comeca_01_termina_10("0110110")) # Valida

