
> **Projeto:** FIAP_Fase 2_Tarefa_Cap 6 — *Python e Além*  
> **Repositório:** https://github.com/murilosalla-blip/fiap-fase02-python-e-alem  
> **Ambiente:** Windows 10 • VS Code (PowerShell) • Python 3.13 • `oracledb` • Oracle Cloud FIAP  

---

## 🧩 1) Descrição do problema
Durante a execução do script `test_oracle.py`, a conexão com o banco de dados falhava com a mensagem:

Erro ao conectar ao Oracle: ORA-12154: TNS:could not resolve the connect identifier specified

Após investigar o `.env`, foi identificado que as variáveis estavam nomeadas como:

```bash
DB_USER=RM568041
DB_PASSWORD=DtNasc#ddmmaa
DB_DSN=oracle.fiap.com.br:1521/ORCL
O código Python, porém, buscava variáveis chamadas ORACLE_USER, ORACLE_PASSWORD e ORACLE_DSN, resultando em valores None e na falha de conexão.

⚙️ 2) Passos para reproduzir
Criar o arquivo .env com as variáveis incorretas:

bash
Copiar código
DB_USER=RM568041
DB_PASSWORD=DtNasc#ddmmaa
DB_DSN=oracle.fiap.com.br:1521/ORCL
Executar:

powershell
Copiar código
python .\src\cap06_python_e_alem\test_oracle.py
Observar o erro no terminal:

arduino
Copiar código
Erro ao conectar ao Oracle: ORA-12154: TNS:could not resolve the connect identifier specified
🔍 3) Causa raiz
Inconsistência entre os nomes das variáveis no .env e os nomes usados no código.

O script utilizava:

python
Copiar código
os.getenv("ORACLE_USER")
os.getenv("ORACLE_PASSWORD")
os.getenv("ORACLE_DSN")
Como o .env continha DB_USER em vez de ORACLE_USER, o Python recebia valores vazios (None), impedindo a conexão.

🧰 4) Solução aplicada
Padronizar o arquivo .env com os nomes corretos:

bash
Copiar código
ORACLE_USER=RM568041
ORACLE_PASSWORD=DtNasc#ddmmaa
ORACLE_DSN=oracle.fiap.com.br:1521/ORCL
Confirmar no código (test_oracle.py e main.py) que o carregamento está assim:

python
Copiar código
import os
from dotenv import load_dotenv
import oracledb

load_dotenv()

conn = oracledb.connect(
    user=os.getenv('ORACLE_USER'),
    password=os.getenv('ORACLE_PASSWORD'),
    dsn=os.getenv('ORACLE_DSN')
)
print("Conexão com o Oracle bem-sucedida!")
Reexecutar o teste:

powershell
Copiar código
python .\src\cap06_python_e_alem\test_oracle.py
Resultado:

Copiar código
Conexão com o Oracle bem-sucedida!
✅ 5) Resultado após correção
Conexão com o Oracle estabelecida corretamente.

.env e código sincronizados e documentados.

Ambiente confirmado funcional para os scripts main.py e funcoes.py.

