# ==============================================================================
#         ATIVIDADES EM PYTHON – CONTEXTUALIZADAS NA WEG
# ==============================================================================

import random
import time
import statistics

# ==============================================================================
# QUESTÃO 1 – Monitoramento de Temperatura
# ==============================================================================
print("=" * 60)
print("QUESTÃO 1 – Monitoramento de Temperatura")
print("=" * 60)

temperaturas = []
for i in range(20):
    temp = random.uniform(60, 100)
    temperaturas.append(temp)

print("Leituras de temperatura dos motores WEG:")
for i in range(len(temperaturas)):
    temp = temperaturas[i]
    print(f"  Leitura {i+1:02d}: {temp:.1f}°C", end="")
    if temp > 80:
        print("  ⚠️  ALERTA: Superaquecimento!")
    else:
        print("  ✅ Normal")

print()


# ==============================================================================
# QUESTÃO 2 – Controle de Velocidade de Esteira
# ==============================================================================
print("=" * 60)
print("QUESTÃO 2 – Controle de Velocidade de Esteira")
print("=" * 60)

velocidades = []
for i in range(20):
    vel = random.uniform(0.2, 1.5)
    velocidades.append(vel)

print("Leituras de velocidade da esteira transportadora:")
for i in range(len(velocidades)):
    vel = velocidades[i]
    print(f"  Leitura {i+1:02d}: {vel:.2f} m/s", end="")
    if vel < 0.5:
        print("  ⚠️  ALERTA: Velocidade abaixo do mínimo!")
    else:
        print("  ✅ Normal")

print()


# ==============================================================================
# QUESTÃO 3 – Consumo de Energia
# ==============================================================================
print("=" * 60)
print("QUESTÃO 3 – Consumo de Energia")
print("=" * 60)

LIMITE_CONSUMO = 150.0  # kWh

consumos = []
for i in range(20):
    consumo = random.uniform(80, 200)
    consumos.append(consumo)

print(f"Limite definido: {LIMITE_CONSUMO} kWh")
print("Leituras de consumo energético:")
for i in range(len(consumos)):
    c = consumos[i]
    print(f"  Leitura {i+1:02d}: {c:.1f} kWh", end="")
    if c > LIMITE_CONSUMO:
        excesso = c - LIMITE_CONSUMO
        print(f"  ⚠️  ALERTA: Excesso de {excesso:.1f} kWh!")
    else:
        print("  ✅ Dentro do limite")

print()


# ==============================================================================
# QUESTÃO 4 – Controle de Qualidade (pH)
# ==============================================================================
print("=" * 60)
print("QUESTÃO 4 – Controle de Qualidade (pH)")
print("=" * 60)

pH_MIN = 6.0
pH_MAX = 8.0

valores_ph = []
for i in range(20):
    ph = random.uniform(4.5, 9.5)
    valores_ph.append(ph)

print(f"Faixa ideal de pH: {pH_MIN} a {pH_MAX}")
print("Leituras de pH no tratamento de superfícies:")
for i in range(len(valores_ph)):
    ph = valores_ph[i]
    print(f"  Leitura {i+1:02d}: pH {ph:.2f}", end="")
    if ph < pH_MIN:
        print(f"  ⚠️  ALERTA: pH muito ácido! (abaixo de {pH_MIN})")
    elif ph > pH_MAX:
        print(f"  ⚠️  ALERTA: pH muito básico! (acima de {pH_MAX})")
    else:
        print("  ✅ pH dentro da faixa ideal")

print()


# ==============================================================================
# QUESTÃO 5 – Monitoramento de Câmara Fria
# ==============================================================================
print("=" * 60)
print("QUESTÃO 5 – Monitoramento de Câmara Fria")
print("=" * 60)

LIMITE_CAMARA = 10.0  # °C
leituras_camara = []
i = 0
while i < 20:
    temp = random.uniform(-5, 20)
    leituras_camara.append(temp)
    i += 1

alertas = 0
print(f"Limite máximo da câmara fria: {LIMITE_CAMARA}°C")
print("Leituras de temperatura da câmara:")
for i in range(len(leituras_camara)):
    temp = leituras_camara[i]
    print(f"  Leitura {i+1:02d}: {temp:.1f}°C", end="")
    if temp > LIMITE_CAMARA:
        alertas += 1
        print("  ⚠️  ALERTA: Temperatura acima do limite!")
    else:
        print("  ✅ Normal")

print(f"\n  Total de alertas registrados: {alertas}")

print()


# ==============================================================================
# QUESTÃO 6 – Nível de Tanque
# ==============================================================================
print("=" * 60)
print("QUESTÃO 6 – Nível de Tanque")
print("=" * 60)

niveis = []
for i in range(20):
    nivel = random.uniform(5, 100)
    niveis.append(nivel)

criticos_baixo = 0
criticos_alto = 0
print("Leituras de nível dos tanques industriais:")
for i in range(len(niveis)):
    n = niveis[i]
    print(f"  Tanque {i+1:02d}: {n:.1f}%", end="")
    if n < 20:
        criticos_baixo += 1
        print("  🔴 CRÍTICO: Nível muito baixo!")
    elif n > 90:
        criticos_alto += 1
        print("  🔴 CRÍTICO: Nível muito alto! Risco de transbordamento!")
    else:
        print("  ✅ Nível adequado")

print(f"\n  Alertas de nível baixo:  {criticos_baixo}")
print(f"  Alertas de nível alto:   {criticos_alto}")
print(f"  Total de críticos:       {criticos_baixo + criticos_alto}")

print()


# ==============================================================================
# QUESTÃO 7 – Vibração de Máquina
# ==============================================================================
print("=" * 60)
print("QUESTÃO 7 – Vibração de Máquina")
print("=" * 60)

LIMITE_VIBRACAO = 5.0  # mm/s

def verificar_vibracao(valor):
    """Verifica se a vibração está dentro do limite seguro."""
    if valor > LIMITE_VIBRACAO:
        return "ALERTA"
    else:
        return "NORMAL"

def gerar_dados_vibracao(quantidade):
    """Gera uma lista de leituras de vibração aleatórias."""
    dados = []
    for i in range(quantidade):
        vibracao = random.uniform(1.0, 9.0)
        dados.append(vibracao)
    return dados

vibracoes = gerar_dados_vibracao(20)

print(f"Limite de vibração: {LIMITE_VIBRACAO} mm/s")
print("Leituras dos sensores de vibração:")
for i in range(len(vibracoes)):
    v = vibracoes[i]
    status = verificar_vibracao(v)
    icone = "⚠️ " if status == "ALERTA" else "✅"
    print(f"  Motor {i+1:02d}: {v:.2f} mm/s  {icone} {status}")

print()


# ==============================================================================
# QUESTÃO 8 – Pressão em Sistema Hidráulico
# ==============================================================================
print("=" * 60)
print("QUESTÃO 8 – Pressão em Sistema Hidráulico")
print("=" * 60)

PRESSAO_MIN = 100  # bar
PRESSAO_MAX = 250  # bar

def analisar_pressao(pressao, p_min, p_max):
    """
    Analisa a pressão e retorna status e mensagem.
    Retorna uma tupla: (status, mensagem)
    """
    if pressao < p_min:
        return ("BAIXA", f"Pressão insuficiente! Mínimo: {p_min} bar")
    elif pressao > p_max:
        return ("ALTA", f"Pressão excessiva! Máximo: {p_max} bar")
    else:
        return ("NORMAL", "Pressão dentro da faixa segura")

pressoes = [random.uniform(70, 280) for _ in range(20)]

print(f"Faixa segura de pressão: {PRESSAO_MIN} a {PRESSAO_MAX} bar")
print("Leituras do sistema hidráulico:")
for i, p in enumerate(pressoes):
    status, mensagem = analisar_pressao(p, PRESSAO_MIN, PRESSAO_MAX)
    icone = "✅" if status == "NORMAL" else "⚠️ "
    print(f"  Ponto {i+1:02d}: {p:.1f} bar  {icone} {mensagem}")

print()


# ==============================================================================
# QUESTÃO 9 – Produtividade da Linha
# ==============================================================================
print("=" * 60)
print("QUESTÃO 9 – Produtividade da Linha")
print("=" * 60)

META_HORA = 85  # unidades por hora

producao_por_hora = [random.randint(60, 110) for _ in range(20)]

total = sum(producao_por_hora)
media = total / len(producao_por_hora)
maximo = max(producao_por_hora)
minimo = min(producao_por_hora)

horas_abaixo_meta = [p for p in producao_por_hora if p < META_HORA]

print(f"Meta de produção: {META_HORA} unidades/hora")
print("\nProdução por hora:")
for i, prod in enumerate(producao_por_hora):
    icone = "✅" if prod >= META_HORA else "❌"
    print(f"  Hora {i+1:02d}: {prod} unidades  {icone}")

print(f"\n  📊 Resumo:")
print(f"     Total produzido:    {total} unidades")
print(f"     Média por hora:     {media:.1f} unidades")
print(f"     Maior produção:     {maximo} unidades")
print(f"     Menor produção:     {minimo} unidades")
print(f"     Horas abaixo meta:  {len(horas_abaixo_meta)}")
print(f"     Meta atingida:      {'✅ SIM' if media >= META_HORA else '❌ NÃO'}")

print()


# ==============================================================================
# QUESTÃO 10 – Lógica de CLP
# ==============================================================================
print("=" * 60)
print("QUESTÃO 10 – Lógica de CLP")
print("=" * 60)

def logica_clp(temperatura):
    """
    Simula a lógica de um CLP para controle de temperatura.
    Retorna a ação a ser tomada e uma descrição.
    """
    if temperatura > 80:
        return ("DESLIGAR", "🔴 Máquina DESLIGADA por superaquecimento!")
    elif temperatura > 70:
        return ("ALERTA", "🟡 ATENÇÃO: Temperatura elevada. Monitorar.")
    else:
        return ("OPERAR", "🟢 Operação NORMAL.")

print("Simulador de lógica CLP - WEG")
print("Testando com 5 valores de temperatura:")

valores_teste = [55.0, 72.5, 81.3, 68.0, 90.0]
for temp in valores_teste:
    acao, descricao = logica_clp(temp)
    print(f"  Temperatura: {temp}°C  →  [{acao}] {descricao}")

# Simulação com entrada do usuário (comentada para execução automática)
# temp_input = float(input("\nDigite uma temperatura para testar: "))
# acao, descricao = logica_clp(temp_input)
# print(f"Resultado: [{acao}] {descricao}")

print()


# ==============================================================================
# QUESTÃO 11 – Sistema de Alarmes Industriais
# ==============================================================================
print("=" * 60)
print("QUESTÃO 11 – Sistema de Alarmes Industriais")
print("=" * 60)

def classificar_alarme(valor, limite_alerta, limite_critico):
    """Classifica o valor em: OK, ALERTA ou CRITICO."""
    if valor >= limite_critico:
        return "CRITICO"
    elif valor >= limite_alerta:
        return "ALERTA"
    else:
        return "OK"

leituras = [random.uniform(0, 100) for _ in range(20)]

contagem = {"OK": 0, "ALERTA": 0, "CRITICO": 0}
historico_alarmes = []

print("Monitoramento de alarmes industriais:")
for i, valor in enumerate(leituras):
    status = classificar_alarme(valor, limite_alerta=60, limite_critico=80)
    contagem[status] += 1
    if status != "OK":
        historico_alarmes.append({"leitura": i+1, "valor": valor, "status": status})
    icone = {"OK": "✅", "ALERTA": "🟡", "CRITICO": "🔴"}[status]
    print(f"  Sensor {i+1:02d}: {valor:.1f}  {icone} {status}")

print(f"\n  📋 Resumo de alarmes:")
for tipo, qtd in contagem.items():
    print(f"     {tipo:<8}: {qtd} ocorrência(s)")

print(f"\n  🔔 Histórico de falhas ({len(historico_alarmes)} registros):")
for registro in historico_alarmes:
    print(f"     Leitura {registro['leitura']:02d}: {registro['valor']:.1f} → {registro['status']}")

print()


# ==============================================================================
# QUESTÃO 12 – Classificação de Estados
# ==============================================================================
print("=" * 60)
print("QUESTÃO 12 – Classificação de Estados das Máquinas")
print("=" * 60)

ESTADOS = {
    "normal":  (0, 60),
    "alerta":  (60, 80),
    "critico": (80, 100),
}

def classificar_estado(valor):
    """Retorna o estado da máquina baseado no valor lido."""
    for estado, (minimo, maximo) in ESTADOS.items():
        if minimo <= valor < maximo:
            return estado
    return "critico"

dados_maquinas = {
    "Motor A": random.uniform(0, 100),
    "Motor B": random.uniform(0, 100),
    "Motor C": random.uniform(0, 100),
    "Esteira 1": random.uniform(0, 100),
    "Esteira 2": random.uniform(0, 100),
    "Bomba Hid.": random.uniform(0, 100),
}

icones_estado = {"normal": "🟢", "alerta": "🟡", "critico": "🔴"}

print("Dashboard de estados das máquinas WEG:")
print(f"  {'Equipamento':<15} {'Valor':>8}   {'Estado'}")
print(f"  {'-'*40}")
for maquina, valor in dados_maquinas.items():
    estado = classificar_estado(valor)
    icone = icones_estado[estado]
    print(f"  {maquina:<15} {valor:>6.1f}%   {icone} {estado.upper()}")

# Resumo por estado usando list comprehension
for estado in ["normal", "alerta", "critico"]:
    lista = [m for m, v in dados_maquinas.items() if classificar_estado(v) == estado]
    print(f"\n  {icones_estado[estado]} {estado.upper()} ({len(lista)}): {', '.join(lista) if lista else 'Nenhuma'}")

print()


# ==============================================================================
# QUESTÃO 13 – Supervisório (SCADA)
# ==============================================================================
print("=" * 60)
print("QUESTÃO 13 – Supervisório (SCADA) – Simulação")
print("=" * 60)

def simular_leitura_sensor(nome, minimo, maximo):
    """Simula a leitura de um sensor."""
    return {
        "nome": nome,
        "valor": round(random.uniform(minimo, maximo), 2),
        "unidade": "°C" if "Temp" in nome else ("bar" if "Press" in nome else "%"),
    }

sensores = [
    ("Temp. Motor A", 60, 100),
    ("Temp. Motor B", 60, 100),
    ("Pressão Hid.",  80, 280),
    ("Nível Tanque",   5, 100),
]

print("Iniciando leitura contínua do supervisório (5 ciclos)...")
print()

for ciclo in range(1, 6):
    print(f"  🔄 Ciclo {ciclo}/5 — Atualização do SCADA")
    print(f"  {'─'*45}")
    for nome, minimo, maximo in sensores:
        leitura = simular_leitura_sensor(nome, minimo, maximo)
        print(f"  │ {leitura['nome']:<18}: {leitura['valor']:>8.2f} {leitura['unidade']}")
    print(f"  {'─'*45}")
    print()
    time.sleep(0.3)  # Pequena pausa para simular atualização em tempo real

print("  SCADA: Leitura contínua encerrada.")
print()


# ==============================================================================
# QUESTÃO 14 – Histórico de Dados
# ==============================================================================
print("=" * 60)
print("QUESTÃO 14 – Histórico de Dados")
print("=" * 60)

class HistoricoSensor:
    """Armazena e analisa o histórico de leituras de um sensor."""

    def __init__(self, nome_sensor):
        self.nome = nome_sensor
        self.dados = []

    def adicionar(self, valor):
        self.dados.append(round(valor, 2))

    def media(self):
        if not self.dados:
            return 0
        return sum(self.dados) / len(self.dados)

    def maximo(self):
        return max(self.dados) if self.dados else 0

    def minimo(self):
        return min(self.dados) if self.dados else 0

    def exibir_historico(self):
        print(f"\n  📁 Histórico do sensor: {self.nome}")
        print(f"  {'Seq':>4}  {'Valor':>8}")
        print(f"  {'─'*18}")
        for i, v in enumerate(self.dados):
            print(f"  {i+1:>4}  {v:>8.2f}°C")
        print(f"  {'─'*18}")
        print(f"  {'Média':>4}: {self.media():>8.2f}°C")
        print(f"  {'Máx':>4}: {self.maximo():>8.2f}°C")
        print(f"  {'Mín':>4}: {self.minimo():>8.2f}°C")

sensor_historico = HistoricoSensor("Motor Eixo Principal")
for _ in range(10):
    sensor_historico.adicionar(random.uniform(60, 100))

sensor_historico.exibir_historico()
print()


# ==============================================================================
# QUESTÃO 15 – Edge Computing
# ==============================================================================
print("=" * 60)
print("QUESTÃO 15 – Edge Computing")
print("=" * 60)

LIMIAR_CRITICO = 85.0

# Gera 100 dados no dispositivo de borda (edge)
dados_brutos = [random.uniform(50, 100) for _ in range(100)]

# Filtro local: apenas dados críticos são enviados para a nuvem
filtrar_critico = lambda v: v > LIMIAR_CRITICO
dados_criticos = list(filter(filtrar_critico, dados_brutos))

# Ordena os dados críticos do maior para o menor
dados_criticos_ordenados = sorted(dados_criticos, reverse=True)

print(f"  Total de leituras geradas no edge:  {len(dados_brutos)}")
print(f"  Limiar crítico definido:             {LIMIAR_CRITICO}°C")
print(f"  Dados críticos filtrados:            {len(dados_criticos)}")
print(f"  Taxa de eventos críticos:            {len(dados_criticos)/len(dados_brutos)*100:.1f}%")
print(f"\n  📡 Dados críticos a enviar para a nuvem (top 10):")
for i, v in enumerate(dados_criticos_ordenados[:10]):
    print(f"     {i+1:02d}. {v:.2f}°C")

print()


# ==============================================================================
# QUESTÃO 16 – IoT Industrial
# ==============================================================================
print("=" * 60)
print("QUESTÃO 16 – IoT Industrial")
print("=" * 60)

def criar_payload_iot(dispositivo_id, tipo_sensor, valor, unidade):
    """Cria um payload de dados no formato IoT para envio à nuvem."""
    return {
        "device_id": dispositivo_id,
        "sensor_type": tipo_sensor,
        "value": round(valor, 3),
        "unit": unidade,
        "timestamp": f"2025-01-{random.randint(1,28):02d}T{random.randint(0,23):02d}:{random.randint(0,59):02d}:00Z",
        "status": "active",
    }

def simular_envio_nuvem(payload):
    """Simula o envio de dados para a nuvem (WEG Cloud)."""
    time.sleep(0.05)  # Simula latência de rede
    return {"success": True, "message_id": random.randint(10000, 99999)}

dispositivos = [
    ("WEG-MOTOR-001", "temperature", random.uniform(60, 100), "°C"),
    ("WEG-MOTOR-002", "vibration",   random.uniform(1, 9),    "mm/s"),
    ("WEG-PUMP-001",  "pressure",    random.uniform(80, 280),  "bar"),
    ("WEG-TANK-001",  "level",       random.uniform(5, 100),   "%"),
    ("WEG-CONV-001",  "speed",       random.uniform(0.2, 1.5), "m/s"),
]

print("  📡 Enviando dados dos dispositivos IoT para WEG Cloud...")
print()
for dev_id, tipo, valor, unidade in dispositivos:
    payload = criar_payload_iot(dev_id, tipo, valor, unidade)
    resposta = simular_envio_nuvem(payload)
    print(f"  📤 Enviando: [{dev_id}] {tipo} = {valor:.2f} {unidade}")
    print(f"     ✅ Enviado com sucesso! message_id: {resposta['message_id']}")
    print()

print()


# ==============================================================================
# QUESTÃO 17 – Dashboard Industrial
# ==============================================================================
print("=" * 70)
print("QUESTÃO 17 – Dashboard Industrial")
print("=" * 70)

def gerar_dados_dashboard(n=20):
    """Gera dados simulados para o dashboard."""
    return {
        "Temperatura (°C)":  [random.uniform(60, 100) for _ in range(n)],
        "Vibração (mm/s)":   [random.uniform(1.0, 9.0) for _ in range(n)],
        "Pressão (bar)":     [random.uniform(80, 280) for _ in range(n)],
        "Nível (%)" :        [random.uniform(5, 100) for _ in range(n)],
    }

def exibir_dashboard(dados):
    """Exibe o dashboard com métricas calculadas."""
    print(f"\n  {'═'*70}")
    print(f"  {'WEG INDUSTRIAL DASHBOARD':^60}")
    print(f"  {'═'*70}")
    print(f"  {'Variável':<20} {'Média':>10} {'Máx':>10} {'Mín':>10} {'DP':>8}")
    print(f"  {'─'*70}")
    for variavel, valores in dados.items():
        media  = statistics.mean(valores)
        maximo = max(valores)
        minimo = min(valores)
        dp     = statistics.stdev(valores)
        print(f"  {variavel:<20} {media:>10.2f} {maximo:>10.2f} {minimo:>10.2f} {dp:>8.2f}")
    print(f"  {'═'*70}\n")

dados_dashboard = gerar_dados_dashboard()
exibir_dashboard(dados_dashboard)

print()


# ==============================================================================
# QUESTÃO 18 – Detecção de Falhas
# ==============================================================================
print("=" * 60)
print("QUESTÃO 18 – Detecção de Falhas (Anomalias)")
print("=" * 60)

def detectar_anomalias(dados, limiar_zscore=2.0):
    """
    Detecta anomalias usando Z-Score.
    Valores com |z| > limiar são considerados anomalias.
    """
    media = statistics.mean(dados)
    desvio = statistics.stdev(dados)

    anomalias = []
    resultados = []
    for i, valor in enumerate(dados):
        z = (valor - media) / desvio if desvio > 0 else 0
        is_anomalia = abs(z) > limiar_zscore
        resultados.append({"idx": i+1, "valor": valor, "z_score": z, "anomalia": is_anomalia})
        if is_anomalia:
            anomalias.append(resultados[-1])

    return resultados, anomalias, media, desvio

# Dados com algumas anomalias injetadas manualmente
dados_sensor = [random.uniform(68, 75) for _ in range(17)]
dados_sensor += [98.5, 45.2, 101.0]  # Anomalias injetadas
random.shuffle(dados_sensor)

resultados, anomalias, media, desvio = detectar_anomalias(dados_sensor)

print(f"  Análise de anomalias (Z-Score > 2.0)")
print(f"  Média: {media:.2f}°C | Desvio Padrão: {desvio:.2f}°C\n")
print(f"  {'Seq':>4}  {'Valor':>8}  {'Z-Score':>9}  {'Status'}")
print(f"  {'─'*42}")
for r in resultados:
    icone = "🔴 ANOMALIA" if r["anomalia"] else "✅ Normal"
    print(f"  {r['idx']:>4}  {r['valor']:>8.2f}  {r['z_score']:>+9.2f}  {icone}")

print(f"\n  ⚡ Total de anomalias detectadas: {len(anomalias)}")
for a in anomalias:
    print(f"     → Leitura {a['idx']:02d}: {a['valor']:.2f}°C (Z={a['z_score']:+.2f})")

print()


# ==============================================================================
# QUESTÃO 19 – Eficiência da Produção
# ==============================================================================
print("=" * 60)
print("QUESTÃO 19 – Eficiência da Produção (OEE)")
print("=" * 60)

def calcular_oee(tempo_planejado, tempo_operando, producao_real, producao_ideal, pecas_ok, producao_total):
    """
    Calcula o OEE (Overall Equipment Effectiveness).
    OEE = Disponibilidade × Performance × Qualidade
    """
    disponibilidade = tempo_operando / tempo_planejado if tempo_planejado > 0 else 0
    performance     = producao_real / producao_ideal if producao_ideal > 0 else 0
    qualidade       = pecas_ok / producao_total if producao_total > 0 else 0
    oee             = disponibilidade * performance * qualidade
    return {
        "disponibilidade": disponibilidade * 100,
        "performance":     performance * 100,
        "qualidade":       qualidade * 100,
        "oee":             oee * 100,
    }

META_OEE = 85.0  # Meta WEG: OEE ≥ 85%

turno = {
    "tempo_planejado": 480,   # minutos
    "tempo_operando":  430,   # minutos (paradas descontadas)
    "producao_real":   820,   # peças produzidas
    "producao_ideal":  900,   # capacidade máxima no tempo operando
    "pecas_ok":        798,   # peças aprovadas no controle de qualidade
    "producao_total":  820,   # total produzido
}

resultado = calcular_oee(**turno)

print("  Dados do Turno:")
print(f"     Tempo planejado:   {turno['tempo_planejado']} min")
print(f"     Tempo operando:    {turno['tempo_operando']} min")
print(f"     Produção real:     {turno['producao_real']} peças")
print(f"     Peças aprovadas:   {turno['pecas_ok']} peças")

print(f"\n  📊 Indicadores OEE:")
print(f"     Disponibilidade:  {resultado['disponibilidade']:.1f}%")
print(f"     Performance:      {resultado['performance']:.1f}%")
print(f"     Qualidade:        {resultado['qualidade']:.1f}%")
print(f"  {'─'*35}")
print(f"     OEE TOTAL:        {resultado['oee']:.1f}%")
print(f"     Meta OEG:          {META_OEE}%")

if resultado["oee"] >= META_OEE:
    print(f"     Status:           ✅ META ATINGIDA!")
else:
    gap = META_OEE - resultado["oee"]
    print(f"     Status:           ❌ Abaixo da meta por {gap:.1f}%")

print()


# ==============================================================================
# QUESTÃO 20 – Sistema Completo Industrial (Integração Total)
# ==============================================================================
print("=" * 60)
print("QUESTÃO 20 – Sistema Completo Industrial WEG")
print("=" * 60)

# ── CAMADA 1: SENSOR (geração de dados) ───────────────────────────────────────
class Sensor:
    """Representa um sensor físico na linha de produção."""
    def __init__(self, sensor_id, tipo, unidade, v_min, v_max):
        self.sensor_id = sensor_id
        self.tipo      = tipo
        self.unidade   = unidade
        self.v_min     = v_min
        self.v_max     = v_max

    def ler(self):
        """Simula a leitura do sensor."""
        return round(random.uniform(self.v_min, self.v_max), 2)


# ── CAMADA 2: CLP (lógica de controle) ────────────────────────────────────────
class CLP:
    """Controlador Lógico Programável – aplica regras de controle."""
    def __init__(self, nome):
        self.nome = nome
        self.regras = []

    def adicionar_regra(self, condicao, acao):
        """Adiciona uma regra de controle: (função_condicao, texto_ação)."""
        self.regras.append((condicao, acao))

    def processar(self, valor):
        """Aplica as regras ao valor e retorna a ação correspondente."""
        for condicao, acao in self.regras:
            if condicao(valor):
                return acao
        return "OPERAÇÃO NORMAL"


# ── CAMADA 3: BANCO DE DADOS (armazenamento) ──────────────────────────────────
class BancoDados:
    """Simula um banco de dados para persistência dos dados industriais."""
    def __init__(self):
        self._registros = []

    def inserir(self, registro):
        self._registros.append(registro)

    def consultar_todos(self):
        return self._registros

    def consultar_por_status(self, status):
        return [r for r in self._registros if r.get("status") == status]

    def total(self):
        return len(self._registros)


# ── CAMADA 4: SUPERVISÓRIO (exibição em tempo real) ───────────────────────────
class Supervisorio:
    """Exibe dados em tempo real no painel SCADA."""
    def exibir(self, sensor_id, valor, unidade, acao):
        icone = "🔴" if "DESLIGAR" in acao or "CRÍTICO" in acao else (
                "🟡" if "ALERTA" in acao else "🟢")
        print(f"  {icone} [{sensor_id}] Valor: {valor:>7.2f} {unidade:<5} → {acao}")


# ── CAMADA 5: DASHBOARD (relatório final) ─────────────────────────────────────
class Dashboard:
    """Gera o relatório executivo final para tomada de decisão."""
    def gerar_relatorio(self, banco):
        registros = banco.consultar_todos()
        if not registros:
            print("  Sem dados para relatório.")
            return

        valores = [r["valor"] for r in registros]
        normais  = len(banco.consultar_por_status("NORMAL"))
        alertas  = len(banco.consultar_por_status("ALERTA"))
        criticos = len(banco.consultar_por_status("CRITICO"))

        print(f"\n  {'═'*55}")
        print(f"  {'RELATÓRIO EXECUTIVO – WEG SISTEMA INDUSTRIAL':^55}")
        print(f"  {'═'*55}")
        print(f"  Total de leituras:    {len(registros)}")
        print(f"  Média dos valores:    {statistics.mean(valores):.2f}")
        print(f"  Desvio padrão:        {statistics.stdev(valores):.2f}")
        print(f"  Valor máximo:         {max(valores):.2f}")
        print(f"  Valor mínimo:         {min(valores):.2f}")
        print(f"  {'─'*55}")
        print(f"  🟢 Leituras normais:  {normais}")
        print(f"  🟡 Alertas:           {alertas}")
        print(f"  🔴 Críticos:          {criticos}")
        saude = (normais / len(registros)) * 100
        print(f"  {'─'*55}")
        print(f"  Índice de saúde:      {saude:.1f}%  {'✅' if saude >= 70 else '⚠️ '}")
        print(f"  {'═'*55}\n")


# ── EXECUÇÃO DO SISTEMA COMPLETO ──────────────────────────────────────────────
print("\n  Inicializando Sistema Industrial WEG...\n")

# Instancia os componentes
sensor     = Sensor("TEMP-MOTOR-001", "Temperatura", "°C", 55, 100)
banco      = BancoDados()
scada      = Supervisorio()
dashboard  = Dashboard()

# Configura as regras do CLP
clp = CLP("CLP-WEG-LINHA-01")
clp.adicionar_regra(lambda v: v > 90,       "🔴 DESLIGAR MÁQUINA – CRÍTICO")
clp.adicionar_regra(lambda v: 75 < v <= 90, "🟡 ALERTA – Reduzir carga")
clp.adicionar_regra(lambda v: v <= 75,      "🟢 OPERAÇÃO NORMAL")

def determinar_status(acao):
    if "CRÍTICO" in acao or "DESLIGAR" in acao:
        return "CRITICO"
    elif "ALERTA" in acao:
        return "ALERTA"
    else:
        return "NORMAL"

# Pipeline de dados: Sensor → CLP → SCADA → Banco
print(f"  📡 Supervisório em tempo real:")
print(f"  {'─'*55}")
for ciclo in range(15):
    valor = sensor.ler()
    acao  = clp.processar(valor)
    scada.exibir(sensor.sensor_id, valor, sensor.unidade, acao)
    banco.inserir({
        "ciclo": ciclo + 1,
        "sensor_id": sensor.sensor_id,
        "valor": valor,
        "acao": acao,
        "status": determinar_status(acao),
    })
    time.sleep(0.05)

# Gera relatório final no Dashboard
dashboard.gerar_relatorio(banco)

print("  ✅ Sistema WEG encerrado com sucesso.")
print()