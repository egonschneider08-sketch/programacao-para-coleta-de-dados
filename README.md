# 🏭 Industrial Data Automation Lab

> Repositório de estudos em **Automação Industrial, IoT e Coleta de Dados em Tempo Real**.

---

## 🚀 Visão Geral

Este projeto simula um ambiente industrial completo, com:

* 📡 Sensores (temperatura, pressão, nível, vibração)
* 🧠 Lógica de controle (CLP)
* 📊 Dashboard (visualização de dados)
* 🗄️ Armazenamento e análise

Objetivo: desenvolver competências práticas em **Indústria 4.0**.

---

## 🧱 Arquitetura do Sistema

```mermaid
graph LR
A[Sensores] --> B[CLP]
B --> C[Edge]
C --> D[Banco de Dados]
D --> E[Dashboard]
```

---

## 📊 Dashboard (Exemplo)

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/256c56ae-d0b1-4e18-9908-bd38a4cc9f67" />



---

## 📈 Gráficos de Monitoramento

### Temperatura

<img width="1860" height="1032" alt="image" src="https://github.com/user-attachments/assets/458abcf0-7952-45bd-9d11-2ea067e33336" />


---

## ⚙️ Tecnologias Utilizadas

* Python 🐍
* JavaScript 🌐
* Chart.js 📊
* MQTT (simulado)
* Node.js (opcional)

---

## 🧠 Funcionalidades

* Monitoramento em tempo real
* Detecção de anomalias
* Sistema de alertas
* Simulação de sensores industriais
* Dashboard interativo

---

## 📂 Estrutura do Projeto

```bash
project/
 ├── python/
 ├── javascript/
 ├── dashboard/
 └── docs/
```

---

## 🧪 Exemplos de Uso

```python
sensor = Sensor("TEMP-01", "temperatura", "°C", 0, 100)
valor = sensor.ler()
print(valor)
```

---

## 📡 Roadmap

* [x] Simulação de sensores
* [x] Dashboard web
* [ ] Integração com banco de dados
* [ ] API REST
* [ ] Deploy em nuvem

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos em automação industrial e programação.

---

## ⭐ Contribuição

Sinta-se livre para contribuir com melhorias!

---

## 📜 Licença

MIT License
