#17 - Implemente em Python a conversão de um AFN para um AFD para um autômato que reconhece strings terminadas em '01'.

def afn_termina_em_01(palavra):
    estado = 'q0'  

    for char in palavra:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'  
            elif char == '1':
                estado = 'q0'  
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
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q2':
        return "palavra valida (termina em '01')"
    else:
        return "palavra invalida (não termina em '01')"

# Testes
print(afn_termina_em_01("101"))    # Valida
print(afn_termina_em_01("110"))    # Invalida
print(afn_termina_em_01("00"))     # Invalida
print(afn_termina_em_01("001"))    # Valida
print(afn_termina_em_01("0101"))   # Valida
print(afn_termina_em_01("111"))    # Invalida

class AFD:
    def __init__(self):
        self.estados = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q1', '1': 'q0'}
        }
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q2'}

    def processar(self, palavra):
        estado_atual = self.estado_inicial

        for char in palavra:
            if char in self.estados[estado_atual]:
                estado_atual = self.estados[estado_atual][char]
            else:
                return 'palavra invalida (caractere inválido)'

        if estado_atual in self.estados_aceitacao:
            return "palavra valida (termina em '01')"
        else:
            return "palavra invalida (não termina em '01')"

# Testes do AFD
afd = AFD()
print(afd.processar("101"))    # Valida
print(afd.processar("110"))    # Invalida
print(afd.processar("00"))     # Invalida
print(afd.processar("001"))    # Valida
print(afd.processar("0101"))   # Valida
print(afd.processar("111"))    # Invalida
