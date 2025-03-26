segundos = int(input("Digite o valor em segundos: "))

dias = segundos // (24 * 3600)
horas = (segundos % (24 * 3600)) // 3600
minutos = (segundos % 3600) // 60

print(f"{dias} dias, {horas} horas, {minutos} minutos")
