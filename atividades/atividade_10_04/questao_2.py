import random

# Gerar 20 leituras de velocidade (entre 0.2 e 1.2 m/s)
velocidades = []
for i in range(20):
    velocidade = round(random.uniform(0.2, 1.2), 2)
    velocidades.append(velocidade)

# Mostrar os valores
print("=" * 50)
print("CONTROLE DE VELOCIDADE DA ESTEIRA")
print("=" * 50)
print(f"Leituras: {velocidades}")
print()

# Verificar cada leitura
contagem_alerta = 0

for i in range(20):
    print(f"Leitura {i+1:2d}: {velocidades[i]} m/s", end=" ")
    
    if velocidades[i] < 0.5:
        print("- ALERTA! Velocidade muito baixa!")
        contagem_alerta += 1
    else:
        print("- Velocidade adequada")

# Resumo final
print()
print("=" * 50)
print("RESUMO DA OPERAÇÃO")
print("=" * 50)
print(f"Total de alertas: {contagem_alerta}")

if contagem_alerta > 0:
    print(f"ATENÇÃO: A esteira teve {contagem_alerta} oscilações abaixo de 0.5 m/s!")
    print("Recomendação: Verificar motor e roldanas da esteira.")
else:
    print("Operação normal. Velocidade mantida dentro do padrão.")