## Projeto AgroTech: Controle de Insumos para Cultura de Milho

Este projeto foi desenvolvido como parte da disciplina "Python e Além" do curso da FIAP.

## O Problema (A "Dor" do Agronegócio)

O controle de custos e o rastreamento da aplicação de insumos (fertilizantes, herbicidas, etc.) são desafios constantes para produtores rurais. A falta de um registro simples e centralizado pode levar a gastos excessivos, aplicação incorreta de produtos e dificuldade na análise de produtividade de cada talhão (lote da fazenda).

## A Solução Proposta

Este programa é um sistema simples (CRUD) que funciona como uma ferramenta para o produtor de milho registrar, consultar e gerenciar todas as aplicações de insumos em sua lavoura. A solução centraliza os dados em um banco de dados Oracle, garantindo a segurança e a integridade das informações.

## Funcionalidades

O sistema oferece as seguintes funcionalidades através de um menu interativo:

1.  **Cadastrar Aplicação de Insumo:** Permite registrar uma nova aplicação, informando data, talhão, tipo de insumo, nome do produto e quantidade.
2.  **Listar Aplicações Registradas:** Exibe na tela todos os registros do banco de dados de forma organizada.
3.  **Editar um Registro:** Permite corrigir informações de um registro já existente.
4.  **Excluir um Registro:** Remove um registro incorreto do banco de dados.
5.  **Exportar para JSON:** Gera um arquivo `relatorio_insumos.json` com todos os dados do banco, facilitando a integração com outros sistemas ou a criação de relatórios.

## Como Executar o Programa

1.  Certifique-se de ter o Python e as bibliotecas `oracledb`, `pandas` e `python-dotenv` instaladas.
2.  Configure suas credenciais de acesso ao Oracle no arquivo `.env`.
3.  Execute o programa principal através do terminal PowerShell:
    python principal.py
    