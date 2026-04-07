# Calculadora Simples

# Exibe uma mensagem inicial
print("=== Calculadora Simples ===")

# Solicita ao usuário o primeiro número e converte para float (número decimal)
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número e converte para float
num2 = float(input("Digite o segundo número: "))

# Mostra as opções de operação disponíveis
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebe a mensagem do usuário
operacao = input("Digite o número da operação desejada (+, -, *, /.): ")

# Verifica qual operação foi escolhida pelo usuário
if operacao == "+":
    # Realiza a soma dos dois números
    resultado = num1 + num2
    # Exibe o resultado da soma
    print("Resultado:", resultado)

elif operacao == "-":
    # Realiza a subtração dos dois números
    resultado = num1 - num2
    # Exibe o resultado da subtração
    print("Resultado:", resultado)

elif operacao == "*":
    # Realiza a multiplicação dos dois números
    resultado = num1 * num2
    # Exibe o resultado da multiplicação
    print("Resultado:", resultado)

elif operacao == "/":
    # Verifica se o segundo número é zero para evitar erro na divisão
    if num2 != 0:
        # Realiza a divisão dos dois números
        resultado = num1 / num2
        # Exibe o resultado da divisão
        print("Resultado:", resultado)
    else:
        # Exibe mensagem de erro se o divisor for zero
        print("Erro: divisão por zero não é permitida.")

else:
    # Caso o usuário digite uma opção inválida
    print("Operação inválida!")
15
