import streamlit as st
import pandas as pd
from ibge import estados
from ibge import cidades

st.title("Empreendimentos")

tab1, tab2, tab3, tab4 = st.tabs(["    Cadastro    ", "    Alterar    ", "    Desativar    ", "    Visualizar    "], )

#Tab de Cadastro
with tab1:
    #Subheader do Cadastro
    st.subheader("Cadastrar Empreendimennto")
    #Campo texto do nome do empreendimento
    nome = st.text_input("Digite o nome do empreendimento")
    #Colunas com campos de estado, cidade, bairro e tipo de empreendimento
    col_estado, col_cidade, col_endereco, col_tipo = st.columns(4)
    with col_estado:
        estado = st.selectbox("Selecione o estado", options=estados())
    with col_cidade:
        cidade = st.selectbox("Selecione a cidade", options= cidades(estado))
    with col_endereco:
        bairro = st.text_input("Digite o nome do bairro")
    with col_tipo:
        tipo = st.selectbox("Selecione a cidade", options= ['Alto Padrão', 'Geminada', 'Casa Plana', 'Residencial'])
    #Campo de texto para endereço
    endereco = st.text_input("Digite o endereço. Ex.: Av. dos Anjos, 400.")
    #Tabela para cadastrar unidades
    df = pd.DataFrame([], columns= ['Unidade', 'Metros²', 'Valor (R$)'])
    unidade = edited_df = st.data_editor(df, num_rows="dynamic")

    cadastrar = st.button("Cadastrar") 
    if cadastrar:
        st.dataframe(unidade)
    else:
        st.write("Aguardando tabela")