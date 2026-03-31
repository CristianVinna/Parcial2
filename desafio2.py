# Programa para verificar se um número é par ou ímpar

# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))  # input() recebe o valor digitado e int() converte para número inteiro

# Verifica se o número é par
if numero % 2 == 0:  # % é o operador de resto da divisão, se o resto for 0 o número é par
    print("O número é par")  # Mostra na tela que o número é par
else:  # Caso o resto da divisão não seja 0
    print("O número é ímpar")  # Mostra na tela que o número é ímpar
