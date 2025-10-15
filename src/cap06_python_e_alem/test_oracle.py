# src/cap06_python_e_alem/test_oracle.py
import os
from pathlib import Path
from dotenv import load_dotenv
import oracledb

# localizar o .env na raiz do projeto
current_file = Path(__file__).resolve()
project_root = current_file.parents[2]
dotenv_path = project_root / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)
else:
    load_dotenv()

def main():
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")

    print(f"Vars -> USER={bool(user)} PASS={bool(password)} DSN={bool(dsn)}")

    if not all([user, password, dsn]):
        print("❌ Variáveis ausentes. Verifique o .env na raiz do repositório.")
        return

    try:
        conn = oracledb.connect(user=user, password=password, dsn=dsn)
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM DUAL")
            print(f"✅ Conexão Oracle bem-sucedida! SELECT -> {cur.fetchone()}")
    except Exception as e:
        print("❌ Erro ao conectar:", e)
    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    main()
