# AI Project Document - Módulo 1 - FIAP

## Grupo
**Nome:** Murilo Salla  
**RM:** 568041  

---

## Sumário
1. Introdução  
 1.1 Escopo do Projeto  
  1.1.1 Contexto da Inteligência Artificial  
  1.1.2 Descrição da Solução Desenvolvida  
2. Visão Geral do Projeto  
 2.1 Objetivos do Projeto  
 2.2 Público-Alvo  
 2.3 Metodologia  
3. Desenvolvimento do Projeto  
 3.1 Tecnologias Utilizadas  
 3.2 Modelagem e Algoritmos  
 3.3 Treinamento e Teste  
4. Resultados e Avaliações  
 4.1 Análise dos Resultados  
 4.2 Feedback dos Usuários  
5. Conclusões e Trabalhos Futuros  
6. Referências  
Anexos  

---

## 1. Introdução

### 1.1 Escopo do Projeto

#### 1.1.1 Contexto da Inteligência Artificial
O avanço da Inteligência Artificial tem possibilitado a automação e otimização de processos em diferentes setores.  
Nesta fase do curso, o foco foi o **domínio da linguagem Python** aplicada à integração com **bancos de dados Oracle**, fornecendo a base para futuras aplicações de IA que dependem de persistência, manipulação e análise de dados.

#### 1.1.2 Descrição da Solução Desenvolvida
O projeto **“Python e Além”** consistiu na criação de um ambiente completo de integração entre Python e Oracle Database.  
Foi desenvolvida uma aplicação modular que realiza testes de conexão, leitura e escrita no banco, utilizando boas práticas de segurança, como variáveis de ambiente e isolamento via virtual environment.  
O repositório foi estruturado de acordo com o **template oficial FIAP**, incluindo documentação, scripts e relatórios técnicos.

---

## 2. Visão Geral do Projeto

### 2.1 Objetivos do Projeto
- Configurar e validar a integração entre Python e Oracle.  
- Utilizar variáveis de ambiente (`.env`) para ocultar credenciais sensíveis.  
- Padronizar o repositório conforme o modelo FIAP (`.github`, `scripts`, `document`, `src`).  
- Registrar problemas técnicos e suas soluções.  
- Criar uma base sólida para os próximos módulos de IA.

### 2.2 Público-Alvo
O projeto foi desenvolvido para fins acadêmicos, direcionado a **estudantes e docentes** da graduação em **Inteligência Artificial da FIAP**.  
Pode servir também como referência para profissionais iniciantes que desejam compreender a integração segura entre Python e bancos relacionais.

### 2.3 Metodologia
A metodologia aplicada foi **Hands-on Learning**, com foco em prática orientada por experimentação.  
O desenvolvimento seguiu etapas curtas de iteração:
1. Configuração de ambiente virtual e bibliotecas.  
2. Criação do arquivo `.env` e validação via `dotenv`.  
3. Conexão Oracle e teste de autenticação (`test_oracle.py`).  
4. Estruturação do projeto e documentação técnica.  
5. Publicação do repositório no GitHub.

---

## 3. Desenvolvimento do Projeto

### 3.1 Tecnologias Utilizadas
| Tecnologia | Função Principal |
|-------------|------------------|
| **Python 3.13** | Linguagem base da aplicação. |
| **oracledb** | Biblioteca para comunicação com Oracle. |
| **python-dotenv** | Leitura de variáveis de ambiente. |
| **Oracle Database (FIAP Cloud)** | Sistema gerenciador de banco de dados. |
| **PowerShell / VS Code** | Execução e automação de ambiente. |
| **GitHub** | Controle de versão e documentação. |

### 3.2 Modelagem e Algoritmos
Embora o foco não tenha sido em modelos de IA ainda, o projeto aplicou **boas práticas de arquitetura de código**:
- Modularização em `main.py` e `funcoes.py`;  
- Leitura segura de credenciais com `os.getenv()`;  
- Tratamento de exceções na conexão Oracle;  
- Uso de loops e funções reutilizáveis para as operações de CRUD futuras.

### 3.3 Treinamento e Teste
O teste principal foi a **validação de conexão com o Oracle Cloud**.  
Foram simulados cenários de erro (como credenciais incorretas) para identificar o problema real, que estava na nomenclatura das variáveis de ambiente (`DB_USER` → `ORACLE_USER`).  
Após a correção, o script retornou:
Conexão com o Oracle bem-sucedida!

---

## 4. Resultados e Avaliações

### 4.1 Análise dos Resultados
O ambiente foi configurado com sucesso.  
A conexão entre Python e Oracle foi estabelecida e validada.  
O uso de `.env` e `.gitignore` garantiu segurança das credenciais.  
O repositório ficou totalmente aderente ao **template FIAP**, incluindo pastas, scripts e documentação.

### 4.2 Feedback dos Usuários
O processo de correção foi acompanhado de forma prática e iterativa, com suporte técnico rápido via documentação e acompanhamento virtual (ChatGPT como assessor de estudos).  
O resultado foi positivo e consolidou a compreensão dos conceitos abordados no capítulo.

---

## 5. Conclusões e Trabalhos Futuros
O projeto demonstrou na prática como configurar, conectar e documentar um ambiente Python + Oracle.  
Como trabalhos futuros, pretende-se:
- Implementar um CRUD completo (inserir, listar, atualizar e excluir dados).  
- Integrar a base de dados com um módulo de IA (Machine Learning com Python).  
- Criar dashboards analíticos em R e Power BI utilizando dados do Oracle.  
- Automatizar testes de conexão e geração de relatórios.  

---

## 6. Referências
- FIAP — Material oficial do curso “Python e Além” (Fase 2).  
- Documentação da biblioteca [python-oracledb](https://python-oracledb.readthedocs.io/en/latest/user_guide/).  
- Template base FIAP — [lfusca/templateFiap](https://github.com/lfusca/templateFiap).  
- Tutoriais de boas práticas de ambiente virtual e `.env` — Python Docs.

---

## Anexos
- **Relatório Técnico de Problemas:** `.github/problem-report.md`  
- **Exemplo de Configuração:** `config/.env.example`  
- **Scripts de Setup:** `scripts/setup_venv.ps1` e `scripts/schema.sql`  
- **Código Principal:** `src/cap06_python_e_alem/main.py`  
- **Funções:** `src/cap06_python_e_alem/funcoes.py`  
- **Teste de Conexão:** `src/cap06_python_e_alem/test_oracle.py`