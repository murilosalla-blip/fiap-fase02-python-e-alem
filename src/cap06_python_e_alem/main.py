# Arquivo: principal.py

import oracledb
import os
from dotenv import load_dotenv
from funcoes import *


load_dotenv()


oracle_user = os.getenv('ORACLE_USER')
oracle_password = os.getenv('ORACLE_PASSWORD')
oracle_dsn = os.getenv('ORACLE_DSN')


conn = None
try:
    conn = oracledb.connect(
        user=oracle_user, 
        password=oracle_password, 
        dsn=oracle_dsn
    )
    print("Conexão com o Oracle bem-sucedida!")
    input("Pressione ENTER para continuar...") 

except Exception as e:
    print(f"Erro ao conectar ao Oracle: {e}")
    print("Verifique se as credenciais no arquivo .env estão corretas.")
    exit()


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("---- CONTROLE DE INSUMOS - MILHO ----")
    print("1 - Cadastrar Aplicação de Insumo")
    print("2 - Listar Aplicações Registradas")
    print("3 - Editar um Registro de Aplicação")
    print("4 - Excluir um Registro de Aplicação")
    print("5 - Exportar Registros para JSON")
    print("6 - Sair")
    print("-" * 37)

    escolha = input("Escolha -> ")

    match escolha:
        case '1':
            cadastrar_aplicacao(conn)
        case '2':
            
            listar_aplicacoes(conn)
            
            input("\nPressione ENTER para voltar ao menu.")
        case '3':
            editar_aplicacao(conn)
        case '4':
            excluir_aplicacao(conn)
        case '5':
            exportar_para_json(conn)
        case '6':
            break
        case _:
            print("\nOpção inválida! Pressione ENTER para continuar.")
            input()


if conn:
    conn.close()
    print("Programa encerrado. Conexão com o Oracle fechada.")