# Arquivo: funcoes.py

import pandas as pd
import json
from datetime import datetime

# =====================================================================
# FUNÇÃO 1: Listar Aplicações 
# =====================================================================
def listar_aplicacoes(conn):
    print("\n--- LISTANDO APLICAÇÕES REGISTRADAS ---")
    tem_registros = False
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, data_aplicacao, talhao, tipo_insumo, nome_produto, quantidade_kg_ha FROM controle_insumos_milho ORDER BY id ASC')
        
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum registro encontrado!")
        else:
            df = pd.DataFrame.from_records(
                registros, 
                columns=['ID', 'Data', 'Talhão', 'Tipo', 'Produto', 'Qtd (Kg/ha)']
            )
            print(df)
            tem_registros = True
            
    except Exception as e:
        print(f"Erro ao listar os registros: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
    
   
    return tem_registros

# =====================================================================
# FUNÇÃO 2: Cadastrar Aplicação 
# =====================================================================
def cadastrar_aplicacao(conn):
    print("\n--- CADASTRO DE NOVA APLICAÇÃO ---")
    try:
        
        data_aplicacao = datetime.now()
        print(f"Data da Aplicação: {data_aplicacao.strftime('%d/%m/%Y')}")

        talhao = input("Digite o nome ou número do talhão: ")
        tipo_insumo = input("Digite o tipo de insumo (Ex: Fertilizante, Herbicida): ")
        nome_produto = input("Digite o nome comercial do produto: ")
        quantidade_kg_ha = float(input("Digite a quantidade aplicada (Kg por Hectare): "))

        if not all([talhao, tipo_insumo, nome_produto]):
            print("\nERRO: Todos os campos de texto devem ser preenchidos!")
            input("\nPressione ENTER para voltar ao menu.")
            return

        sql_insert = (
            "INSERT INTO controle_insumos_milho "
            "(data_aplicacao, talhao, tipo_insumo, nome_produto, quantidade_kg_ha) "
            "VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4, :5)"
        )
        dados = (data_aplicacao.strftime('%Y-%m-%d'), talhao, tipo_insumo, nome_produto, quantidade_kg_ha)

        cursor = conn.cursor()
        cursor.execute(sql_insert, dados)
        conn.commit()

    except ValueError:
        print("\nERRO! A quantidade deve ser um número.")
        print("Cadastro cancelado.")
    except Exception as e:
        print(f"\nErro inesperado ao cadastrar: {e}")
        print("Cadastro cancelado.")
    else:
        print("\nDados gravados com sucesso!")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

    input("\nPressione ENTER para voltar ao menu.")

# =====================================================================
# FUNÇÃO 3: Editar Aplicação 
# =====================================================================
def editar_aplicacao(conn):
    print("\n--- EDIÇÃO DE REGISTRO DE APLICAÇÃO ---")
    
    tem_registros = listar_aplicacoes(conn)
    
    if not tem_registros:
        input("\nPressione ENTER para voltar ao menu.")
        return

    try:
        id_editar = int(input("\nDigite o ID do registro que deseja editar: "))
        
        cursor = conn.cursor()
        cursor.execute("SELECT talhao, tipo_insumo, nome_produto, quantidade_kg_ha FROM controle_insumos_milho WHERE id = :1", [id_editar])
        registro_atual = cursor.fetchone()

        if not registro_atual:
            print(f"\nNenhum registro encontrado com o ID {id_editar}.")
        else:
            print("\nDigite os novos dados. Pressione ENTER para manter o valor atual.")
            
            talhao_atual, tipo_atual, produto_atual, qtd_atual = registro_atual

            novo_talhao = input(f"Talhão (Atual: {talhao_atual}): ") or talhao_atual
            novo_tipo = input(f"Tipo de Insumo (Atual: {tipo_atual}): ") or tipo_atual
            novo_produto = input(f"Nome do Produto (Atual: {produto_atual}): ") or produto_atual
            nova_qtd_str = input(f"Quantidade (Atual: {qtd_atual}): ")
            
            nova_qtd = float(nova_qtd_str) if nova_qtd_str else qtd_atual

            sql_update = """
                UPDATE controle_insumos_milho
                SET talhao = :1, tipo_insumo = :2, nome_produto = :3, quantidade_kg_ha = :4
                WHERE id = :5
            """
            dados_update = (novo_talhao, novo_tipo, novo_produto, nova_qtd, id_editar)
            
            cursor.execute(sql_update, dados_update)
            conn.commit()
            print(f"\nRegistro com ID {id_editar} foi atualizado com sucesso!")

    except ValueError:
        print("\nERRO! O ID e a quantidade devem ser números.")
    except Exception as e:
        print(f"\nErro inesperado ao editar: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

    input("\nPressione ENTER para voltar ao menu.")

# =====================================================================
# FUNÇÃO 4: Excluir Aplicação 
# =====================================================================
def excluir_aplicacao(conn):
    print("\n--- EXCLUSÃO DE REGISTRO DE APLICAÇÃO ---")
    
    tem_registros = listar_aplicacoes(conn)
    
    if not tem_registros:
        input("\nPressione ENTER para voltar ao menu.")
        return

    try:
        id_excluir = int(input("\nDigite o ID do registro que deseja excluir: "))
        
        confirmacao = input(f"Tem certeza que deseja excluir o registro com ID {id_excluir}? [S/N]: ").upper()
        
        if confirmacao == 'S':
            sql_delete = "DELETE FROM controle_insumos_milho WHERE id = :1"
            
            cursor = conn.cursor()
            cursor.execute(sql_delete, [id_excluir])
            
            if cursor.rowcount == 0:
                print(f"\nNenhum registro encontrado com o ID {id_excluir}.")
            else:
                conn.commit()
                print(f"\nRegistro com ID {id_excluir} foi excluído com sucesso!")
        else:
            print("\nOperação de exclusão cancelada.")

    except ValueError:
        print("\nERRO! O ID deve ser um número.")
    except Exception as e:
        print(f"\nErro inesperado ao excluir: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

    input("\nPressione ENTER para voltar ao menu.")
    
# =====================================================================
# FUNÇÃO 5: Exportar para JSON 
# =====================================================================
def exportar_para_json(conn):
    print("\n--- EXPORTANDO DADOS PARA JSON ---")
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, data_aplicacao, talhao, tipo_insumo, nome_produto, quantidade_kg_ha FROM controle_insumos_milho ORDER BY id ASC')
        
        colunas = [desc[0].lower() for desc in cursor.description]
        registros = cursor.fetchall()

        if not registros:
            print("Nenhum registro para exportar!")
        else:
            dados_lista = []
            for registro in registros:
                dados_lista.append(dict(zip(colunas, registro)))

            json_output = json.dumps(dados_lista, indent=4, default=str)

            with open('relatorio_insumos.json', 'w', encoding='utf-8') as file:
                file.write(json_output)
            
            print("\nDados exportados com sucesso para o arquivo 'relatorio_insumos.json'")

    except Exception as e:
        print(f"Erro ao exportar para JSON: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

    input("\nPressione ENTER para voltar ao menu.")