def validar_num(num):
    estado='q0'

    for char in num:
        if estado =='q0':
            if char =='0':
                estado = 'q1'
        elif estado =='q1':
            if char =='0':
                estado ='q0'
    if estado=='q1':
        return 'numero é par, termina em 0'
    else:
        return 'numero é impar, não temina com 0'

print(validar_num('100'))
print(validar_num('101'))
print(validar_num('0001'))
