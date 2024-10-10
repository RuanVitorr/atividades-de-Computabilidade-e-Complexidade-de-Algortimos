def validar_num_igual(num):
    estado ='q0'
    incremento = 0

    for char in num:
        if estado =='q0':
            if char == '1':
                incremento += 1
                estado = 'q1'
            elif char =='0':
                estado = 'q0'

        elif estado =='q1':
            if char =='1':
                incremento += 1
                estado = 'q2'
            elif char =='0':
                estado =='q1'

        elif estado =='q2':
            if char=='1':
                incremento += 1
                estado='q3'
            if char =='0':
                estado ='q2'    
    
    if estado =='q2':
        return 'o numero tem exatamente 2 numeros 1'
    elif estado =='q3':
        return 'o numero passou de 2 numeros 1'
    else:
        return 'o numero ainda não tem 2 numeros 1'
        
    
print(validar_num_igual('101'))
print(validar_num_igual('1011'))
print(validar_num_igual('1000'))
print(validar_num_igual('1011'))