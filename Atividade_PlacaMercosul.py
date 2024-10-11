def valida_placa(placa, texto):
    paises = ['Argentina', 'Brasil', 'Venezuela', 'Paraguai', 'Uruguai']
    
    # Validação da placa com formato ABC1D23
    if len(placa) == 7 and placa[:3].isalpha() and placa[3].isdigit() and placa[4].isalpha() and placa[5:].isdigit():
        if texto in paises:
            return "Mercosul"
        else:
            return "Modelo Antigo"
    else:
        return "Placa está com caracteres fora do padrão!"

# Testes
print(valida_placa("ABC1D23", "Brasil"))  # Saída esperada: "Mercosul"
print(valida_placa("A2C1D23", "Joao Pessoa - Paraíba"))  # Saída esperada: "Placa está com caracteres fora do padrão!"
print(valida_placa("A4C1D23", "Brasil"))  # Saída esperada: "Placa está com caracteres fora do padrão!"
print(valida_placa("ABC1D23", "Joao Pessoa - Paraíba"))  # Saída esperada: "Modelo Antigo"
