# Solicita ao usuário um valor em segundos
segundos = int(input("Digite o total de segundos: "))

# Calcula quantas horas tem no total de segundos (1 hora = 3600 segundos)
horas = segundos // 3600

# Calcula o resto dos segundos após remover as horas
resto = segundos % 3600

# Calcula quantos minutos existem no restante (1 minuto = 60 segundos)
minutos = resto // 60

# Calcula os segundos finais restantes
segundos_restantes = resto % 60

# Mostra o resultado formatado para o usuário
print("Tempo convertido:")
print(horas, "hora(s),", minutos, "minuto(s) e", segundos_restantes, "segundo(s)")
