def reconhece_placa(string):
    if len(string) == 8 and string[:3].isalpha() and string[3] == '-' and string[4:].isdigit():
        return string + " placa correta."
    else:
        return string + " placa fora do padrão."

# Testes
print(reconhece_placa('ABC-DEFG'))  # Saída: ABC-DEFG placa fora do padrão
print(reconhece_placa('ABC-1234'))  # Saída: ABC-1234 placa correta.
