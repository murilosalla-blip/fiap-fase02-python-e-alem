import os
import oracledb
from dotenv import load_dotenv


load_dotenv()

user = os.getenv("ORACLE_USER")
pwd  = os.getenv("ORACLE_PASSWORD")
dsn  = os.getenv("ORACLE_DSN")


for k, v in {"ORACLE_USER": user, "ORACLE_PASSWORD": pwd, "ORACLE_DSN": dsn}.items():
    if not v:
        raise RuntimeError(f"Variável de ambiente ausente: {k}")

try:
    with oracledb.connect(user=user, password=pwd, dsn=dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM dual")
            print("✅ Conexão com Oracle FIAP bem-sucedida!")
            print("Resultado do SELECT:", cur.fetchone())
except oracledb.Error as e:
    print("❌ Erro Oracle (credenciais/DSN/rede?):", e)
except Exception as e:
    print("❌ Erro inesperado:", e)
