# Solicita ao usuário o capital inicial (valor investido)
capital = float(input("Digite o capital (R$): "))

# Solicita ao usuário a taxa de juros (em porcentagem)
taxa = float(input("Digite a taxa de juros (%): "))

# Solicita ao usuário o tempo (em períodos, ex: meses ou anos)
tempo = float(input("Digite o tempo: "))

# Converte a taxa de porcentagem para decimal dividindo por 100
taxa_decimal = taxa / 100

# Calcula os juros simples usando a fórmula J = C * i * t
juros = capital * taxa_decimal * tempo

# Exibe o valor dos juros calculados
print("O valor dos juros é: R$", juros)
