# Programa para calcular a área de um triângulo

# Exibe uma mensagem inicial ao usuário
print("=== Cálculo da Área de um Triângulo ===")

# Solicita ao usuário o valor da base do triângulo e converte para número decimal (float)
base = float(input("Digite o valor da base do triângulo: "))

# Solicita ao usuário o valor da altura do triângulo e converte para float
altura = float(input("Digite o valor da altura do triângulo: "))

# Calcula a área do triângulo usando a fórmula (base * altura) / 2
area = (base * altura) / 2

# Exibe o resultado do cálculo da área
print("A área do triângulo é:", area)
