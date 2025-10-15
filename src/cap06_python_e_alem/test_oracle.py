# src/cap06_python_e_alem/test_oracle.py
import os
from pathlib import Path
from dotenv import load_dotenv
import oracledb

# Localiza o .env no root do repositório, mesmo rodando fora da raiz
current_file = Path(__file__).resolve()
project_root = current_file.parents[2]  # cap06_python_e_alem -> src -> <repo root>
dotenv_path = project_root / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)
else:
    load_dotenv()  # fallback: tenta CWD

def main():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_dsn = os.getenv("DB_DSN")

    # Diagnóstico (sem vazar segredos)
    print("USER:", bool(db_user))
    print("PASS:", bool(db_password))
    print("DSN :", bool(db_dsn))

    if not all([db_user, db_password, db_dsn]):
        print("❌ Variáveis ausentes. Verifique seu .env na raiz do repositório.")
        print("   Esperado no .env: DB_USER=..., DB_PASSWORD=..., DB_DSN=oracle.fiap.com.br:1521/ORCL")
        return

    try:
        # Modo thin (não precisa Instant Client)
        conn = oracledb.connect(user=db_user, password=db_password, dsn=db_dsn)

        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM DUAL")
            row = cur.fetchone()
        print(f"✅ Conexão Oracle bem-sucedida! Teste SELECT -> {row}")

    except oracledb.Error as e:
        # Mostra código e mensagem do Oracle se disponíveis
        err_msg = getattr(e, "args", [str(e)])[0]
        print("❌ Erro ao conectar:", err_msg)
    finally:
        try:
            conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
