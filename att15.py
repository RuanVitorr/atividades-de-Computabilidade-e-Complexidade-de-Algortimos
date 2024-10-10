#15 - Implemente um AFN que reconheça a linguagem de todas as strings sobre {a, b} com comprimento par.

def afn_comprimento_par(palavra):
    estado = 'q0' 

    for char in palavra:
        if estado == 'q0':
            if char == 'a':
                estado = 'q1'  
            elif char == 'b':
                estado = 'q1'  
            else:
                return 'palavra invalida (caractere inválido)'
        elif estado == 'q1':
            if char == 'a':
                estado = 'q0'  
            elif char == 'b':
                estado = 'q0'  
            else:
                return 'palavra invalida (caractere inválido)'

    if estado == 'q0':
        return "palavra valida (comprimento par)"
    else:
        return "palavra invalida (comprimento ímpar)"

# Testes
print(afn_comprimento_par(""))           # Valida (comprimento par)
print(afn_comprimento_par("a"))          # Invalida (comprimento ímpar)
print(afn_comprimento_par("b"))          # Invalida (comprimento ímpar)
print(afn_comprimento_par("ab"))         # Valida (comprimento par)
print(afn_comprimento_par("aabb"))       # Valida (comprimento par)
print(afn_comprimento_par("abab"))       # Valida (comprimento par)
print(afn_comprimento_par("aaa"))        # Invalida (comprimento ímpar)
print(afn_comprimento_par("bbba"))       # Invalida (comprimento ímpar)
print(afn_comprimento_par("ababa"))      # Invalida (comprimento ímpar)
