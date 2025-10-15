import os
import oracledb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("ORACLE_USER")
PWD  = os.getenv("ORACLE_PASSWORD")
DSN  = os.getenv("ORACLE_DSN")

for k, v in {"ORACLE_USER": USER, "ORACLE_PASSWORD": PWD, "ORACLE_DSN": DSN}.items():
    if not v:
        raise RuntimeError(f"Variável de ambiente ausente: {k}")

def df_from_cursor(cur) -> pd.DataFrame:
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    return pd.DataFrame(rows, columns=cols)

with oracledb.connect(user=USER, password=PWD, dsn=DSN) as conn:
    with conn.cursor() as cur:
        
        cur.execute(
            "INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES (:1, :2, :3)",
            ("Cachorro", "Bob", 12),
        )
        conn.commit()

        
        cur.execute("SELECT id, tipo_pet, nome_pet, idade FROM petshop ORDER BY id")
        df = df_from_cursor(cur)
        if not df.empty:
            df = df.set_index("ID")
        print("\n-- LISTA INICIAL --")
        print(df if not df.empty else "Tabela vazia")

        if not df.empty:
            last_id = int(df.index.max())

            
            cur.execute(
                "UPDATE petshop SET idade = :idade WHERE id = :id",
                {"idade": int(df.loc[last_id, 'IDADE']) + 1, "id": last_id},
            )
            conn.commit()

            
            cur.execute("DELETE FROM petshop WHERE id = :id", {"id": last_id})
            conn.commit()

       
        cur.execute("SELECT id, tipo_pet, nome_pet, idade FROM petshop ORDER BY id")
        end_df = df_from_cursor(cur)
        if not end_df.empty:
            end_df = end_df.set_index("ID")
        print("\n-- APÓS UPDATE/DELETE --")
        print(end_df if not end_df.empty else "Tabela vazia")
