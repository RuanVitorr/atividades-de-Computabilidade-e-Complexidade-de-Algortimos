def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido!"
    
    cpf_mascarado = ['X'] * 3 + list(cpf[3:9]) + ['X'] * 2
    return ''.join(cpf_mascarado)

# Testes
print(valida_cpf("70468293493"))  # Saída: XXX682934XX
print(valida_cpf("12345678901"))  # Saída: XXX456789XX
print(valida_cpf("00000000000"))  # Saída: XXX000000XX
print(valida_cpf("01234567890"))  # Saída: XXX456789XX
print(valida_cpf("12345678abc"))  # Saída: CPF inválido! (não numérico)
print(valida_cpf("123456789"))    # Saída: CPF inválido! (tamanho errado)
