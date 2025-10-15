# FIAP - Faculdade de Informática e Administração Paulista

🎥 **Demonstração no YouTube:** [Clique aqui para assistir](https://youtu.be/EOJU7vbXAMo)  

## Nome do Projeto
Controle de Insumos – Milho (Capítulo 6 - Python e Além)

## Nome do Grupo
Turma 1TIAOR - 2025

👨‍🎓 **Integrante:**
- Murilo Salla (RM568041)

👩‍🏫 **Professores:**
- **Tutor(a):** Ana Cristina dos Santos  
- **Coordenador:** André Godoi Chiovato  

---

## 📜 Descrição
Este projeto corresponde ao **Capítulo 6 – Python e Além** da disciplina de Inteligência Artificial.  

O sistema tem como objetivo **registrar, consultar, editar, excluir e exportar aplicações de insumos agrícolas (milho)** em um banco de dados Oracle.  
Ele simula um controle básico de insumos agrícolas, com funcionalidades voltadas à prática de integração entre **Python, Oracle Database e boas práticas de organização de código**.  

Entre as principais funcionalidades, estão:  
- Cadastro de novas aplicações de insumo (fertilizante, herbicida, etc.)  
- Listagem de registros em formato tabular (via `pandas`)  
- Edição e exclusão de registros existentes  
- Exportação dos registros para **JSON**  
- Estrutura modularizada em Python com uso de **.env** para segurança de credenciais  

---

## 📁 Estrutura de Pastas
```

/ (raiz)
├─ .github/               → configurações do GitHub
├─ assets/                → imagens e recursos visuais
├─ config/                → arquivos de configuração (.env.example)
├─ document/other/        → documentos auxiliares (ex: Links.txt)
├─ scripts/               → schema.sql e scripts auxiliares
├─ src/cap06_python_e_alem/
│  ├─ funcoes.py          → funções de CRUD e exportação JSON
│  ├─ main.py             → programa principal (menu interativo)
│  └─ test_oracle.py      → teste de conexão ao Oracle
├─ requirements.txt       → dependências Python
├─ README.md              → guia geral do projeto
└─ .gitignore             → exclusão de arquivos desnecessários

````

---

## 🔧 Como executar o código

### Pré-requisitos
- **Python 3.13+**
- **Oracle Instant Client** configurado no sistema
- **Banco de Dados FIAP Oracle**
- IDE recomendada: **VS Code**

### Instalação
1. Clonar este repositório:
   ```bash
   git clone https://github.com/murilosalla-blip/fiap-fase02-python-e-alem.git
   cd fiap-fase02-python-e-alem
````

2. Criar e ativar o ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instalar dependências:

   ```powershell
   pip install -r requirements.txt
   ```

4. Configurar o arquivo `.env`:

   ```ini
   ORACLE_USER=seu_usuario
   ORACLE_PASSWORD=sua_senha
   ORACLE_DSN=oracle.fiap.com.br:1521/ORCL
   ```

### Execução

1. Criar a tabela no Oracle (se ainda não existir):

   ```sql
   @scripts/schema.sql
   ```

2. Rodar o programa principal:

   ```powershell
   python .\src\cap06_python_e_alem\main.py
   ```

3. Testar a conexão isoladamente (opcional):

   ```powershell
   python .\src\cap06_python_e_alem\test_oracle.py
   ```

---

## 🗃 Histórico de lançamentos

* 0.5.0 - 14/10/2025 – Estrutura final no padrão `templateFiap`
* 0.4.0 - 13/10/2025 – CRUD completo + exportação JSON
* 0.3.0 - 11/10/2025 – Conexão Oracle e testes iniciais
* 0.2.0 - 09/10/2025 – Estrutura inicial do projeto
* 0.1.0 - 08/10/2025 – Ambiente configurado (Python + Oracle)

---
