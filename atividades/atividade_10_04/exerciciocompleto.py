import random
import statistics
import time

# ======================================================
# FUNÇÕES AUXILIARES
# ======================================================
def gerar_dados(qtd, minimo, maximo):
    return [round(random.uniform(minimo, maximo), 2) for _ in range(qtd)]

def mostrar_dados(nome, dados, unidade=""):
    print(f"\n{nome}")
    for i, v in enumerate(dados):
        print(f"{i+1:02d} → {v} {unidade}")


# ======================================================
# QUESTÃO 1 – TEMPERATURA
# ======================================================
temps = gerar_dados(20, 60, 100)
mostrar_dados("Q1 - Temperatura", temps, "°C")

for t in temps:
    if t > 80:
        print(f"⚠️ ALERTA: {t}°C")


# ======================================================
# QUESTÃO 2 – VELOCIDADE
# ======================================================
vels = gerar_dados(20, 0.2, 1.5)
mostrar_dados("Q2 - Velocidade", vels, "m/s")

for v in vels:
    if v < 0.5:
        print(f"⚠️ Baixa velocidade: {v} m/s")


# ======================================================
# QUESTÃO 3 – CONSUMO
# ======================================================
LIMITE = 150
consumos = gerar_dados(20, 80, 200)
mostrar_dados("Q3 - Consumo", consumos, "kWh")

for c in consumos:
    if c > LIMITE:
        print(f"⚠️ Consumo alto: {c} kWh")


# ======================================================
# QUESTÃO 4 – pH
# ======================================================
phs = gerar_dados(20, 4, 9)
mostrar_dados("Q4 - pH", phs)

for ph in phs:
    if ph < 6 or ph > 8:
        print(f"⚠️ pH fora do ideal: {ph}")


# ======================================================
# QUESTÃO 5 – CÂMARA FRIA
# ======================================================
temps = gerar_dados(20, -5, 20)
mostrar_dados("Q5 - Câmara", temps, "°C")

for t in temps:
    if t > 10:
        print(f"⚠️ Temperatura alta: {t}°C")


# ======================================================
# QUESTÃO 6 – NÍVEL
# ======================================================
niveis = gerar_dados(20, 0, 100)
mostrar_dados("Q6 - Nível", niveis, "%")

for n in niveis:
    if n < 20 or n > 90:
        print(f"⚠️ Nível crítico: {n}%")


# ======================================================
# QUESTÃO 7 – VIBRAÇÃO
# ======================================================
def verificar_vibracao(v):
    return "ALERTA" if v > 5 else "OK"

vibs = gerar_dados(20, 1, 9)
mostrar_dados("Q7 - Vibração", vibs, "mm/s")

for v in vibs:
    if verificar_vibracao(v) == "ALERTA":
        print(f"⚠️ Vibração alta: {v}")


# ======================================================
# QUESTÃO 8 – PRESSÃO
# ======================================================
def verificar_pressao(p):
    if p < 100:
        return "BAIXA"
    elif p > 250:
        return "ALTA"
    return "OK"

press = gerar_dados(20, 70, 280)
mostrar_dados("Q8 - Pressão", press, "bar")

for p in press:
    if verificar_pressao(p) != "OK":
        print(f"⚠️ Pressão irregular: {p}")


# ======================================================
# QUESTÃO 9 – PRODUÇÃO
# ======================================================
META = 85
producao = [random.randint(60, 110) for _ in range(20)]

print("\nQ9 - Produção:", producao)
media = statistics.mean(producao)

print("Média:", media)
print("Meta atingida:", "SIM" if media >= META else "NÃO")


# ======================================================
# QUESTÃO 10 – CLP
# ======================================================
def clp(temp):
    if temp > 80:
        return "DESLIGAR"
    return "NORMAL"

print("\nQ10 - CLP")

for t in gerar_dados(5, 60, 100):
    print(t, clp(t))


# ======================================================
# QUESTÃO 11 – ALARMES
# ======================================================
leituras = gerar_dados(20, 0, 100)
cont = 0

print("\nQ11 - Alarmes")

for v in leituras:
    if v > 70:
        cont += 1

print("Total de alarmes:", cont)


# ======================================================
# QUESTÃO 12 – ESTADOS
# ======================================================
def estado(v):
    if v < 60:
        return "NORMAL"
    elif v < 80:
        return "ALERTA"
    return "CRITICO"

dados = gerar_dados(10, 0, 100)

print("\nQ12 - Estados")
for d in dados:
    print(d, estado(d))


# ======================================================
# QUESTÃO 13 – SCADA
# ======================================================
print("\nQ13 - SCADA")

for i in range(3):
    print("Leitura:", random.uniform(60, 100))
    time.sleep(0.3)


# ======================================================
# QUESTÃO 14 – HISTÓRICO
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ14 - Histórico:", dados)
print("Média:", statistics.mean(dados))


# ======================================================
# QUESTÃO 15 – EDGE
# ======================================================
dados = gerar_dados(100, 50, 100)
criticos = [d for d in dados if d > 85]

print("\nQ15 - Edge")
print("Total:", len(dados))
print("Críticos:", len(criticos))


# ======================================================
# QUESTÃO 16 – IoT
# ======================================================
print("\nQ16 - IoT")

valor = random.uniform(60, 100)
print(f"Enviando dado {valor} para nuvem... ✅")


# ======================================================
# QUESTÃO 17 – DASHBOARD
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ17 - Dashboard")
print("Média:", statistics.mean(dados))
print("Máx:", max(dados))
print("Mín:", min(dados))


# ======================================================
# QUESTÃO 18 – ANOMALIA
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ18 - Anomalias")

for d in dados:
    if d > 95 or d < 65:
        print(d, "⚠️ ANOMALIA")


# ======================================================
# QUESTÃO 19 – OEE
# ======================================================
disp, perf, qual = 0.9, 0.85, 0.95
oee = disp * perf * qual

print("\nQ19 - OEE:", round(oee * 100, 2), "%")


# ======================================================
# QUESTÃO 20 – SISTEMA COMPLETO
# ======================================================
print("\nQ20 - Sistema Completo")

banco = []

for i in range(10):
    valor = random.uniform(60, 100)

    # CLP
    if valor > 90:
        status = "CRITICO"
    elif valor > 75:
        status = "ALERTA"
    else:
        status = "NORMAL"

    # SCADA
    print(f"{i+1} → {valor:.1f} ({status})")

    # BANCO
    banco.append({"valor": valor, "status": status})

# DASHBOARD
valores = [d["valor"] for d in banco]

print("\nRelatório Final")
print("Média:", statistics.mean(valores))
print("Total registros:", len(banco))import random
import statistics
import time

# ======================================================
# FUNÇÕES AUXILIARES
# ======================================================
def gerar_dados(qtd, minimo, maximo):
    return [round(random.uniform(minimo, maximo), 2) for _ in range(qtd)]

def mostrar_dados(nome, dados, unidade=""):
    print(f"\n{nome}")
    for i, v in enumerate(dados):
        print(f"{i+1:02d} → {v} {unidade}")


# ======================================================
# QUESTÃO 1 – TEMPERATURA
# ======================================================
temps = gerar_dados(20, 60, 100)
mostrar_dados("Q1 - Temperatura", temps, "°C")

for t in temps:
    if t > 80:
        print(f"⚠️ ALERTA: {t}°C")


# ======================================================
# QUESTÃO 2 – VELOCIDADE
# ======================================================
vels = gerar_dados(20, 0.2, 1.5)
mostrar_dados("Q2 - Velocidade", vels, "m/s")

for v in vels:
    if v < 0.5:
        print(f"⚠️ Baixa velocidade: {v} m/s")


# ======================================================
# QUESTÃO 3 – CONSUMO
# ======================================================
LIMITE = 150
consumos = gerar_dados(20, 80, 200)
mostrar_dados("Q3 - Consumo", consumos, "kWh")

for c in consumos:
    if c > LIMITE:
        print(f"⚠️ Consumo alto: {c} kWh")


# ======================================================
# QUESTÃO 4 – pH
# ======================================================
phs = gerar_dados(20, 4, 9)
mostrar_dados("Q4 - pH", phs)

for ph in phs:
    if ph < 6 or ph > 8:
        print(f"⚠️ pH fora do ideal: {ph}")


# ======================================================
# QUESTÃO 5 – CÂMARA FRIA
# ======================================================
temps = gerar_dados(20, -5, 20)
mostrar_dados("Q5 - Câmara", temps, "°C")

for t in temps:
    if t > 10:
        print(f"⚠️ Temperatura alta: {t}°C")


# ======================================================
# QUESTÃO 6 – NÍVEL
# ======================================================
niveis = gerar_dados(20, 0, 100)
mostrar_dados("Q6 - Nível", niveis, "%")

for n in niveis:
    if n < 20 or n > 90:
        print(f"⚠️ Nível crítico: {n}%")


# ======================================================
# QUESTÃO 7 – VIBRAÇÃO
# ======================================================
def verificar_vibracao(v):
    return "ALERTA" if v > 5 else "OK"

vibs = gerar_dados(20, 1, 9)
mostrar_dados("Q7 - Vibração", vibs, "mm/s")

for v in vibs:
    if verificar_vibracao(v) == "ALERTA":
        print(f"⚠️ Vibração alta: {v}")


# ======================================================
# QUESTÃO 8 – PRESSÃO
# ======================================================
def verificar_pressao(p):
    if p < 100:
        return "BAIXA"
    elif p > 250:
        return "ALTA"
    return "OK"

press = gerar_dados(20, 70, 280)
mostrar_dados("Q8 - Pressão", press, "bar")

for p in press:
    if verificar_pressao(p) != "OK":
        print(f"⚠️ Pressão irregular: {p}")


# ======================================================
# QUESTÃO 9 – PRODUÇÃO
# ======================================================
META = 85
producao = [random.randint(60, 110) for _ in range(20)]

print("\nQ9 - Produção:", producao)
media = statistics.mean(producao)

print("Média:", media)
print("Meta atingida:", "SIM" if media >= META else "NÃO")


# ======================================================
# QUESTÃO 10 – CLP
# ======================================================
def clp(temp):
    if temp > 80:
        return "DESLIGAR"
    return "NORMAL"

print("\nQ10 - CLP")

for t in gerar_dados(5, 60, 100):
    print(t, clp(t))


# ======================================================
# QUESTÃO 11 – ALARMES
# ======================================================
leituras = gerar_dados(20, 0, 100)
cont = 0

print("\nQ11 - Alarmes")

for v in leituras:
    if v > 70:
        cont += 1

print("Total de alarmes:", cont)


# ======================================================
# QUESTÃO 12 – ESTADOS
# ======================================================
def estado(v):
    if v < 60:
        return "NORMAL"
    elif v < 80:
        return "ALERTA"
    return "CRITICO"

dados = gerar_dados(10, 0, 100)

print("\nQ12 - Estados")
for d in dados:
    print(d, estado(d))


# ======================================================
# QUESTÃO 13 – SCADA
# ======================================================
print("\nQ13 - SCADA")

for i in range(3):
    print("Leitura:", random.uniform(60, 100))
    time.sleep(0.3)


# ======================================================
# QUESTÃO 14 – HISTÓRICO
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ14 - Histórico:", dados)
print("Média:", statistics.mean(dados))


# ======================================================
# QUESTÃO 15 – EDGE
# ======================================================
dados = gerar_dados(100, 50, 100)
criticos = [d for d in dados if d > 85]

print("\nQ15 - Edge")
print("Total:", len(dados))
print("Críticos:", len(criticos))


# ======================================================
# QUESTÃO 16 – IoT
# ======================================================
print("\nQ16 - IoT")

valor = random.uniform(60, 100)
print(f"Enviando dado {valor} para nuvem... ✅")


# ======================================================
# QUESTÃO 17 – DASHBOARD
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ17 - Dashboard")
print("Média:", statistics.mean(dados))
print("Máx:", max(dados))
print("Mín:", min(dados))


# ======================================================
# QUESTÃO 18 – ANOMALIA
# ======================================================
dados = gerar_dados(20, 60, 100)

print("\nQ18 - Anomalias")

for d in dados:
    if d > 95 or d < 65:
        print(d, "⚠️ ANOMALIA")


# ======================================================
# QUESTÃO 19 – OEE
# ======================================================
disp, perf, qual = 0.9, 0.85, 0.95
oee = disp * perf * qual

print("\nQ19 - OEE:", round(oee * 100, 2), "%")


# ======================================================
# QUESTÃO 20 – SISTEMA COMPLETO
# ======================================================
print("\nQ20 - Sistema Completo")

banco = []

for i in range(10):
    valor = random.uniform(60, 100)

    # CLP
    if valor > 90:
        status = "CRITICO"
    elif valor > 75:
        status = "ALERTA"
    else:
        status = "NORMAL"

    # SCADA
    print(f"{i+1} → {valor:.1f} ({status})")

    # BANCO
    banco.append({"valor": valor, "status": status})

# DASHBOARD
valores = [d["valor"] for d in banco]

print("\nRelatório Final")
print("Média:", statistics.mean(valores))
print("Total registros:", len(banco))