import random

# Gerar 20 valores aleatórios de temperatura
temperaturas = []
for i in range(20):
    temp = random.randint(60, 100)
    temperaturas.append(temp)

# Exibir os dados coletados
print("Temperaturas dos motores:")
print(temperaturas)
print()

# Verificar cada temperatura
for i in range(20):
    print(f"Motor {i+1}: {temperaturas[i]}°C", end=" ")

    if temperaturas[i] > 80:
        print("- ALERTA! Super aquecimento!")
    else:
        print("- Temperatura normal")