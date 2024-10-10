def valida_string(palavra):
    estado = 'q0'

    for char in palavra:
        if estado == 'q0':
            if char=='0':
                estado ='q0'
            elif char == '1':
                estado = 'q1'
            else:
                estado = 'rejeita'
                break
        elif estado =='q1':
            if char =='0':
                estado ='q0'
            elif char =='1':
                estado ='q1'
            else:
                estado = 'rejeita'
                break
        
    if estado=='q1':
        return "palavra valida(termina com 1)"
    else:
        return'palavra invalida(termina com 0)'

print(valida_string("1001"))
print(valida_string("001"))
print(valida_string("010010"))
print(valida_string("10101"))