# Malware PoC: Ransoware & Keylogger Simulation 🛡️🐍

![Security Analysis](https://img.shields.io/badge/Focus-Malware_Analysis-red)
![Language](https://img.shields.io/badge/Language-Python_3-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational_PoC-green)

## 📝 Descrição do Projeto
Este repositório contém o desenvolvimento de uma **Proof of Concept (PoC)** de ameaças cibernéticas simuladas. O objetivo é estudar a mecânica de funcionamento de códigos maliciosos para aprimorar o desenvolvimento de assinaturas de detecção e estratégias de defesa em endpoints.

Projeto desenvolvido durante o treinamento **Santander Cyber Segurança DIO 2025**, sob orientação da instrutora Isadora Ferrão.

---

## 🛠️ Componentes da Simulação

### 1. Ransomware Simulation (Concept)
* **Funcionalidade:** Simulação de rotina de criptografia em arquivos de teste específicos.
* **Foco de Estudo:** Entendimento de algoritmos de transformação de dados e fluxos de persistência.
* **Objetivo Defensivo:** Analisar como soluções de EDR (Endpoint Detection and Response) identificam padrões de escrita em massa no disco.

### 2. Pseudo-Keylogger (Data Capture)
* **Funcionalidade:** Registro de entradas via terminal para simulação de exfiltração de dados sensíveis.
* **Foco de Estudo:** Interação entre scripts e sistema de arquivos para armazenamento de logs.
* **Objetivo Defensivo:** Compreender vetores de ataque voltados para roubo de credenciais e engenharia social.

---

## 🚀 Aprendizados Técnicos
* **Manipulação de Arquivos com Python:** Leitura, escrita e criptografia/ofuscação.
* **Mentalidade de Atacante (Red Team):** Entender o passo a passo da infecção para criar defesas mais robustas.
* **Prevenção:** Estudo de medidas de mitigação, como backups offline, políticas de privilégio mínimo e monitoramento de processos suspeitos.

---

## 📂 Estrutura do Repositório
* `ransomware_poc.py`: Script simulando a lógica de criptografia.
* `keylogger_sim.py`: Script simulando a captura de entradas de texto.
* `DOCS/`: Explicação detalhada dos métodos de defesa contra essas ameaças.

---

## ⚠️ Aviso Legal (Legal Disclaimer)
**Este projeto tem fins estritamente educacionais e laboratoriais.** O código foi projetado para rodar de forma controlada, sem automação oculta ou danos ao sistema operacional. O uso de técnicas de hacking sem autorização é crime. O autor não se responsabiliza pelo uso indevido deste material.

---
**Contato:** Raphael Albuquerque - https://www.linkedin.com/in/raphael-albuquerque-0b4251348/
