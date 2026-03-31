# Programa que recebe 5 nomes e imprime todos na tela

# Cria uma lista vazia para armazenar os nomes
nomes = []

# Pede o primeiro nome ao usuário e guarda na lista
nome1 = input("Digite o primeiro nome: ")  # input recebe o nome digitado
nomes.append(nome1)  # adiciona o nome na lista

# Pede o segundo nome ao usuário
nome2 = input("Digite o segundo nome: ")  # recebe o segundo nome
nomes.append(nome2)  # adiciona na lista

# Pede o terceiro nome ao usuário
nome3 = input("Digite o terceiro nome: ")  # recebe o terceiro nome
nomes.append(nome3)  # adiciona na lista

# Pede o quarto nome ao usuário
nome4 = input("Digite o quarto nome: ")  # recebe o quarto nome
nomes.append(nome4)  # adiciona na lista

# Pede o quinto nome ao usuário
nome5 = input("Digite o quinto nome: ")  # recebe o quinto nome
nomes.append(nome5)  # adiciona na lista

# Mostra uma mensagem antes de imprimir os nomes
print("\nLista de nomes digitados:")  # pula uma linha e mostra o título

# Imprime todos os nomes da lista
for nome in nomes:  # percorre cada nome dentro da lista
    print(nome)  # imprime cada nome na tela
