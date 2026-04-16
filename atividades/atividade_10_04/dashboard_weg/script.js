// ==========================
// FUNÇÕES BASE (SEU SISTEMA)
// ==========================
function rand(min, max, dec = 1) {
  return parseFloat((Math.random() * (max - min) + min).toFixed(dec));
}

function randArr(n, min, max, dec = 1) {
  return Array.from({ length: n }, () => rand(min, max, dec));
}

// ==========================
// GERADORES (sensores)
// ==========================
function gerarTemperaturas() { return randArr(10, 60, 100); }
function gerarVelocidades() { return randArr(10, 0.2, 1.5, 2); }
function gerarPressao()     { return randArr(10, 80, 200); }
function gerarNivel()       { return randArr(10, 5, 100, 0); }

// ==========================
// GRÁFICOS
// ==========================
let tempChart, velChart, pressChart, nivelChart;

function criarGrafico(id, label, dados) {
  return new Chart(document.getElementById(id), {
    type: 'line',
    data: {
      labels: dados.map((_, i) => i + 1),
      datasets: [{
        label: label,
        data: dados,
        tension: 0.3
      }]
    }
  });
}

// ==========================
// LÓGICA INDUSTRIAL (CLP)
// ==========================
function verificarSistema(temp, vel, press, nivel) {
  let alerta = false;

  if (temp.some(t => t > 80)) alerta = true;
  if (vel.some(v => v < 0.5)) alerta = true;
  if (press.some(p => p < 80 || p > 160)) alerta = true;
  if (nivel.some(n => n < 20 || n > 90)) alerta = true;

  return alerta;
}

// ==========================
// DASHBOARD UPDATE
// ==========================
function atualizar() {
  const temp = gerarTemperaturas();
  const vel = gerarVelocidades();
  const press = gerarPressao();
  const nivel = gerarNivel();

  tempChart.data.datasets[0].data = temp;
  velChart.data.datasets[0].data = vel;
  pressChart.data.datasets[0].data = press;
  nivelChart.data.datasets[0].data = nivel;

  tempChart.update();
  velChart.update();
  pressChart.update();
  nivelChart.update();

  // ALERTA VISUAL
  const alerta = verificarSistema(temp, vel, press, nivel);

const status = document.getElementById("status");

if (alerta) {
  status.className = "status alerta";
  status.innerText = "🔴 Alerta no Sistema";
} else {
  status.className = "status normal";
  status.innerText = "🟢 Sistema Normal";
}

// ==========================
// INICIALIZAÇÃO
// ==========================
window.onload = () => {
  tempChart  = criarGrafico("tempChart", "Temperatura (°C)", gerarTemperaturas());
  velChart   = criarGrafico("velChart", "Velocidade (m/s)", gerarVelocidades());
  pressChart = criarGrafico("pressChart", "Pressão (bar)", gerarPressao());
  nivelChart = criarGrafico("nivelChart", "Nível (%)", gerarNivel());

  // atualização automática (tempo real)
  setInterval(atualizar, 2000);
};