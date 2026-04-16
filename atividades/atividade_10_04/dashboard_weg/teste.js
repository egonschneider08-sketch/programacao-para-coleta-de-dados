// ============================================================
//  ATIVIDADES EM JAVASCRIPT – CONTEXTUALIZADAS NA WEG
//  20 questões organizadas por funções de alto nível
// ============================================================

// ────────────────────────────────────────────────────────────
//  FUNÇÕES UTILITÁRIAS (base reutilizável)
// ────────────────────────────────────────────────────────────

function rand(min, max, decimais = 1) {
    return parseFloat((Math.random() * (max - min) + min).toFixed(decimais));
  }
  
  function randArr(n, min, max, decimais = 1) {
    return Array.from({ length: n }, () => rand(min, max, decimais));
  }
  
  function calcularMedia(arr) {
    return (arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(2);
  }
  
  function calcularEficiencia(produzido, meta) {
    return ((produzido / meta) * 100).toFixed(1);
  }
  
  // ────────────────────────────────────────────────────────────
  //  FUNÇÕES GERADORAS DE DADOS (camada de sensor)
  // ────────────────────────────────────────────────────────────
  
  function gerarTemperaturas(n = 20)      { return randArr(n, 60, 100); }
  function gerarVelocidades(n = 20)       { return randArr(n, 0.1, 1.5, 2); }
  function gerarConsumo(n = 20)           { return randArr(n, 40, 110); }
  function gerarPH(n = 20)               { return randArr(n, 4.5, 9.5, 2); }
  function gerarTempCamara(n = 20)        { return randArr(n, 5, 18); }
  function gerarNivelTanque(n = 20)       { return randArr(n, 5, 100, 0); }
  function gerarVibracao(n = 20)          { return randArr(n, 1, 12, 2); }
  function gerarPressao(n = 20)           { return randArr(n, 50, 200, 1); }
  function gerarProducaoPorHora(n = 8)    { return randArr(n, 60, 120, 0); }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 1 – Monitoramento de Temperatura
  // ────────────────────────────────────────────────────────────
  
  function q1_monitoramentoTemperatura() {
    const LIMITE = 80;
    const temperaturas = gerarTemperaturas();
    let alertas = 0;
  
    console.log("=== Q1 — Monitoramento de Temperatura ===");
    temperaturas.forEach((t, i) => {
      const alerta = t > LIMITE;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${t.toFixed(1)}°C${alerta ? " ⚠ SUPERAQUECIMENTO" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) em ${temperaturas.length} leituras.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 2 – Controle de Velocidade de Esteira
  // ────────────────────────────────────────────────────────────
  
  function q2_velocidadeEsteira() {
    const LIMITE_MIN = 0.5;
    const velocidades = gerarVelocidades();
    let alertas = 0;
  
    console.log("=== Q2 — Controle de Velocidade de Esteira ===");
    velocidades.forEach((v, i) => {
      const alerta = v < LIMITE_MIN;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${v.toFixed(2)} m/s${alerta ? " ⚠ VELOCIDADE BAIXA" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de velocidade abaixo do mínimo.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 3 – Consumo de Energia
  // ────────────────────────────────────────────────────────────
  
  function q3_consumoEnergia(limiteKWh = 80) {
    const dados = gerarConsumo();
    let alertas = 0;
  
    console.log(`=== Q3 — Consumo de Energia (limite: ${limiteKWh} kWh) ===`);
    dados.forEach((c, i) => {
      const alerta = c > limiteKWh;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${c.toFixed(1)} kWh${alerta ? " ⚠ CONSUMO ALTO" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) acima do limite.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 4 – Controle de Qualidade (pH)
  // ────────────────────────────────────────────────────────────
  
  function q4_controlePH(faixaMin = 6, faixaMax = 8) {
    const phs = gerarPH();
    let alertas = 0;
  
    console.log(`=== Q4 — Controle de pH (faixa ideal: ${faixaMin}–${faixaMax}) ===`);
    phs.forEach((p, i) => {
      const alerta = p < faixaMin || p > faixaMax;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] pH ${p.toFixed(2)}${alerta ? " ⚠ FORA DA FAIXA" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de pH fora do padrão.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 5 – Monitoramento de Câmara Fria
  // ────────────────────────────────────────────────────────────
  
  function q5_camaraFria(limiteMax = 10) {
    const temps = gerarTempCamara();
    let alertas = 0;
  
    console.log(`=== Q5 — Câmara Fria (limite: ${limiteMax}°C) ===`);
    temps.forEach((t, i) => {
      const alerta = t > limiteMax;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${t.toFixed(1)}°C${alerta ? " ⚠ TEMPERATURA ALTA" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de temperatura elevada.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 6 – Nível de Tanque
  // ────────────────────────────────────────────────────────────
  
  function q6_nivelTanque(criticoMin = 20, criticoMax = 90) {
    const niveis = gerarNivelTanque();
    let alertas = 0;
  
    console.log(`=== Q6 — Nível de Tanque (crítico: <${criticoMin}% ou >${criticoMax}%) ===`);
    niveis.forEach((n, i) => {
      let alerta = "";
      if (n < criticoMin)      alerta = " ⚠ NÍVEL CRÍTICO BAIXO";
      else if (n > criticoMax) alerta = " ⚠ NÍVEL CRÍTICO ALTO";
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${String(n).padStart(3)}%${alerta}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de nível crítico.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 7 – Vibração de Máquina
  // ────────────────────────────────────────────────────────────
  
  function q7_vibracaoMaquina(limite = 7) {
    const dados = gerarVibracao();
    let alertas = 0;
  
    console.log(`=== Q7 — Vibração de Máquina (limite: ${limite} mm/s) ===`);
    dados.forEach((v, i) => {
      const alerta = v > limite;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${v.toFixed(2)} mm/s${alerta ? " ⚠ VIBRAÇÃO ALTA" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de vibração acima do limite.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 8 – Pressão em Sistema Hidráulico
  // ────────────────────────────────────────────────────────────
  
  function q8_pressaoHidraulica(faixaMin = 80, faixaMax = 160) {
    const pressoes = gerarPressao();
    let alertas = 0;
  
    console.log(`=== Q8 — Pressão Hidráulica (faixa segura: ${faixaMin}–${faixaMax} bar) ===`);
    pressoes.forEach((p, i) => {
      const alerta = p < faixaMin || p > faixaMax;
      if (alerta) alertas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${p.toFixed(1)} bar${alerta ? " ⚠ FORA DO INTERVALO SEGURO" : ""}`);
    });
    console.log(`\nResumo: ${alertas} alerta(s) de pressão fora do seguro.\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 9 – Produtividade da Linha
  // ────────────────────────────────────────────────────────────
  
  function q9_produtividadeLinha(meta = 100) {
    const producao = gerarProducaoPorHora();
    const media = parseFloat(calcularMedia(producao));
  
    console.log("=== Q9 — Produtividade da Linha ===");
    producao.forEach((p, i) => console.log(`[Hora ${i + 1}] ${p} unidades`));
    console.log(`\nMédia:  ${media.toFixed(2)} unidades/hora`);
    console.log(`Meta:   ${meta} unidades/hora`);
    console.log(media >= meta ? "Status: ✓ META ATINGIDA" : "Status: ✗ META NÃO ATINGIDA");
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 10 – Lógica de CLP
  // ────────────────────────────────────────────────────────────
  
  function q10_logicaCLP(temperatura) {
    console.log("=== Q10 — Lógica de CLP ===");
    console.log(`Temperatura recebida: ${temperatura}°C`);
  
    if (temperatura > 80) {
      console.log("→ Ação: DESLIGAR MÁQUINA (temperatura crítica)");
    } else {
      console.log("→ Ação: OPERAÇÃO NORMAL");
    }
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 11 – Sistema de Alarmes Industriais
  // ────────────────────────────────────────────────────────────
  
  function q11_alarmes(limite = 70) {
    const valores = randArr(15, 0, 100, 0);
    let falhas = 0;
  
    console.log(`=== Q11 — Sistema de Alarmes (alarme se > ${limite}) ===`);
    valores.forEach((v, i) => {
      const alarme = v > limite;
      if (alarme) falhas++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${String(v).padStart(3)} → ${alarme ? "ALARME" : "ok"}`);
    });
    console.log(`\nTotal de falhas: ${falhas} / ${valores.length}\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 12 – Classificação de Estados
  // ────────────────────────────────────────────────────────────
  
  function classificarEstado(valor) {
    if (valor < 30)       return "CRITICO";
    else if (valor < 70)  return "NORMAL";
    else                  return "ALERTA";
  }
  
  function q12_classificacaoEstados() {
    const dados = randArr(15, 0, 100, 0);
  
    console.log("=== Q12 — Classificação de Estados ===");
    dados.forEach((v, i) => {
      const estado = classificarEstado(v);
      console.log(`[${String(i + 1).padStart(2, "0")}] ${String(v).padStart(3)} → [${estado}]`);
    });
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 13 – Supervisório (SCADA)
  // ────────────────────────────────────────────────────────────
  
  function q13_supervisorioSCADA(ciclos = 8) {
    const leituras = [];
  
    console.log("=== Q13 — Supervisório SCADA — Leitura Contínua ===");
    for (let i = 0; i < ciclos; i++) {
      const valor = rand(50, 120);
      const ts = new Date(Date.now() - (ciclos - 1 - i) * 5000).toLocaleTimeString();
      leituras.push({ ciclo: i + 1, valor, ts });
      console.log(`[${ts}] Ciclo ${i + 1}: ${valor.toFixed(1)}`);
    }
    console.log(`\nÚltima atualização: ${leituras[leituras.length - 1].ts}\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 14 – Histórico de Dados
  // ────────────────────────────────────────────────────────────
  
  function q14_historicoDados() {
    const historico = [];
  
    console.log("=== Q14 — Histórico de Dados ===");
  
    // Simula armazenamento de 10 registros
    for (let i = 0; i < 10; i++) {
      historico.push(rand(40, 100));
    }
  
    historico.forEach((v, i) => {
      console.log(`[Reg ${String(i + 1).padStart(2, "0")}] ${v.toFixed(1)}`);
    });
  
    console.log(`\nMédia histórica: ${calcularMedia(historico)}\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 15 – Edge Computing
  // ────────────────────────────────────────────────────────────
  
  function filtrarCriticos(dados, limiteMax = 80, limiteMin = 10) {
    return dados.filter(v => v > limiteMax || v < limiteMin);
  }
  
  function q15_edgeComputing() {
    const todosDados = randArr(100, 0, 100, 0);
    const criticos = filtrarCriticos(todosDados);
  
    console.log("=== Q15 — Edge Computing ===");
    console.log(`Dados gerados: ${todosDados.length}`);
    console.log(`Dados críticos filtrados: ${criticos.length}\n`);
  
    criticos.forEach((v, i) => {
      const tipo = v > 80 ? "alto" : "baixo";
      console.log(`[${String(i + 1).padStart(2, "0")}] ${v} (${tipo})`);
    });
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 16 – IoT Industrial
  // ────────────────────────────────────────────────────────────
  
  function enviarParaNuvem(payload) {
    // Simula envio HTTP para a nuvem
    console.log(`  → Enviando: ${JSON.stringify(payload)}`);
    console.log(`  → Enviado para cloud.weg.net ✓`);
  }
  
  function q16_iotIndustrial() {
    const dados = randArr(5, 10, 100);
  
    console.log("=== Q16 — IoT Industrial ===");
    dados.forEach((d, i) => {
      const payload = { sensor: `S0${i + 1}`, valor: d.toFixed(1), timestamp: Date.now() };
      console.log(`\nDispositivo ${i + 1}:`);
      enviarParaNuvem(payload);
    });
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 17 – Dashboard Industrial
  // ────────────────────────────────────────────────────────────
  
  function gerarRelatorio(dados) {
    return {
      media:  parseFloat(calcularMedia(dados)),
      maximo: Math.max(...dados),
      minimo: Math.min(...dados),
    };
  }
  
  function q17_dashboardIndustrial() {
    const dados = randArr(20, 30, 120);
    const relatorio = gerarRelatorio(dados);
  
    console.log("=== Q17 — Dashboard Industrial ===");
    console.log(`Dados: ${dados.map(d => d.toFixed(1)).join(", ")}`);
    console.log(`\nMédia:  ${relatorio.media.toFixed(2)}`);
    console.log(`Máximo: ${relatorio.maximo.toFixed(1)}`);
    console.log(`Mínimo: ${relatorio.minimo.toFixed(1)}`);
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 18 – Detecção de Falhas
  // ────────────────────────────────────────────────────────────
  
  function detectarAnomalias(dados, tolerancia = 0.2) {
    const media = parseFloat(calcularMedia(dados));
    const desvio = media * tolerancia;
    return dados.map(v => ({ valor: v, anomalia: Math.abs(v - media) > desvio }));
  }
  
  function q18_deteccaoFalhas() {
    const dados = randArr(20, 50, 100);
    const resultado = detectarAnomalias(dados);
    const media = calcularMedia(dados);
    let count = 0;
  
    console.log(`=== Q18 — Detecção de Falhas (média: ${media}, tolerância: ±20%) ===`);
    resultado.forEach((r, i) => {
      if (r.anomalia) count++;
      console.log(`[${String(i + 1).padStart(2, "0")}] ${r.valor.toFixed(1)}${r.anomalia ? " ⚠ ANOMALIA" : ""}`);
    });
    console.log(`\n${count} anomalia(s) detectada(s).\n`);
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 19 – Eficiência da Produção
  // ────────────────────────────────────────────────────────────
  
  function q19_eficienciaProducao(meta = 500) {
    const produzido = rand(300, 600, 0);
    const eficiencia = parseFloat(calcularEficiencia(produzido, meta));
  
    console.log("=== Q19 — Eficiência da Produção ===");
    console.log(`Produzido: ${produzido} unidades`);
    console.log(`Meta:      ${meta} unidades`);
    console.log(`Eficiência: ${eficiencia}%`);
  
    if (eficiencia >= 100) {
      console.log("Status: ✓ META ATINGIDA");
    } else {
      console.log(`Status: ✗ Abaixo da meta (faltam ${(meta - produzido).toFixed(0)} unidades)`);
    }
    console.log();
  }
  
  // ────────────────────────────────────────────────────────────
  //  QUESTÃO 20 – Sistema Completo Industrial
  // ────────────────────────────────────────────────────────────
  
  function coletarDadosSensor(n = 10) {
    return randArr(n, 40, 120);
  }
  
  function aplicarLogicaCLP(dados, limite = 80) {
    return dados.map(v => ({ valor: v, acao: v > limite ? "DESLIGAR" : "NORMAL" }));
  }
  
  function exibirSupervisorio(resultados) {
    resultados.forEach((r, i) => {
      console.log(`  S${i + 1}: ${r.valor.toFixed(1)} → ${r.acao}`);
    });
  }
  
  function armazenarBanco(dados) {
    return dados.map((v, i) => ({ id: i + 1, valor: v, timestamp: Date.now() }));
  }
  
  function exibirDashboard(dados) {
    const relatorio = gerarRelatorio(dados);
    const alertas = dados.filter(v => v > 80).length;
    console.log(`  Média:   ${relatorio.media.toFixed(2)}`);
    console.log(`  Máximo:  ${relatorio.maximo.toFixed(1)}`);
    console.log(`  Mínimo:  ${relatorio.minimo.toFixed(1)}`);
    console.log(`  Alertas: ${alertas} de ${dados.length}`);
  }
  
  function q20_sistemaCompleto() {
    console.log("=== Q20 — Sistema Completo Industrial ===\n");
  
    console.log("[SENSOR] Coletando dados...");
    const sensorDados = coletarDadosSensor();
    sensorDados.forEach((v, i) => console.log(`  S${i + 1}: ${v.toFixed(1)}`));
  
    console.log("\n[CLP] Aplicando lógica de controle...");
    const clpResultados = aplicarLogicaCLP(sensorDados);
    exibirSupervisorio(clpResultados);
  
    console.log("\n[SUPERVISÓRIO] Exibindo dados em tempo real... OK");
  
    console.log("\n[BANCO] Armazenando histórico...");
    const banco = armazenarBanco(sensorDados);
    console.log(`  ${banco.length} registros salvos.`);
  
    console.log("\n[DASHBOARD] Relatório Final:");
    exibirDashboard(sensorDados);
  
    console.log("\n=== FIM DO CICLO ===\n");
  }
  
  // ────────────────────────────────────────────────────────────
  //  EXECUÇÃO DE TODAS AS QUESTÕES
  // ────────────────────────────────────────────────────────────
  
  q1_monitoramentoTemperatura();
  q2_velocidadeEsteira();
  q3_consumoEnergia(80);
  q4_controlePH(6, 8);
  q5_camaraFria(10);
  q6_nivelTanque(20, 90);
  q7_vibracaoMaquina(7);
  q8_pressaoHidraulica(80, 160);
  q9_produtividadeLinha(100);
  q10_logicaCLP(85);   // altere o valor para testar
  q11_alarmes(70);
  q12_classificacaoEstados();
  q13_supervisorioSCADA();
  q14_historicoDados();
  q15_edgeComputing();
  q16_iotIndustrial();
  q17_dashboardIndustrial();
  q18_deteccaoFalhas();
  q19_eficienciaProducao(500);
  q20_sistemaCompleto();