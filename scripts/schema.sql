
CREATE TABLE controle_insumos_milho (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    data_aplicacao DATE,
    talhao VARCHAR2(50),
    tipo_insumo VARCHAR2(50),
    nome_produto VARCHAR2(100),
    quantidade_kg_ha NUMBER(10, 2)
);