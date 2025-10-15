import sys, importlib
print("Versão do Python:", sys.version)
for mod in ["oracledb", "pandas", "dotenv"]:
    try:
        importlib.import_module(mod)
        print(f"✔ Biblioteca '{mod}' carregada com sucesso!")
    except Exception as e:
        print(f"❌ Falha ao carregar '{mod}': {e}")
