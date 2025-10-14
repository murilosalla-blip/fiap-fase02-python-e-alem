# FIAP - Faculdade de Informática e Administração Paulista

# Capítulo 6 — Python e Além  
## Curso de Inteligência Artificial (Online) — 1TIAOR-2025

---

## 👨‍🎓 Integrantes
- **Murilo Salla** — RM568041  

---

## 👩‍🏫 Professores

### Tutora
- **Ana Cristina dos Santos**

### Coordenador
- **André Godoi Chiovato**

---

## 🧠 Descrição

Este repositório contém as implementações e materiais referentes ao **Capítulo 6 — Python e Além**, da disciplina da FIAP — Graduação em Inteligência Artificial.

O objetivo é demonstrar o domínio dos fundamentos de **Python**, boas práticas de estruturação de projeto, uso de **ambiente virtual (venv)**, **variáveis de ambiente (.env)**, e integração com o **GitHub**.

---

## 🗂 Estrutura de pastas

| Pasta | Descrição |
|--------|------------|
| `.github/` | Arquivos de configuração do GitHub (actions, workflows etc.) |
| `assets/` | Imagens e mídias de apoio utilizadas em relatórios e README |
| `config/` | Arquivos de configuração e exemplos de variáveis de ambiente (`.env.example`) |
| `document/` | Relatórios, anotações e demais documentos do capítulo |
| `document/other/` | Materiais complementares (ex.: `Links.txt`) |
| `scripts/` | Scripts auxiliares (`setup_venv.ps1`, `run_app.ps1`, `schema.sql` etc.) |
| `src/` | Código-fonte do capítulo (`main.py`, `funcoes.py`) |

---

## ⚙️ Como executar o projeto

### **Pré-requisitos**
- Python **3.11+**
- PowerShell ou Terminal do VS Code
- Git instalado e configurado

---

### **Passo a passo**

```powershell
# 1. Clonar o repositório
git clone https://github.com/murilosalla-blip/fiap-fase02-python-e-alem
cd fiap-fase02-python-e-alem

# 2. Criar e ativar o ambiente virtual
.\scripts\setup_venv.ps1

# 3. Criar o arquivo .env a partir do exemplo
copy .\config\.env.example .\.env

# 4. Executar a aplicação
.\scripts\run_app.ps1
