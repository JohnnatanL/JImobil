import streamlit as st
import psycopg2
st.set_page_config(layout="wide")

# Função para validar usuário e senha
def validar_login(usuario, senha):
    try:
        # Conectando ao banco de dados
        conn = psycopg2.connect(
            host="aws-0-sa-east-1.pooler.supabase.com",
            port="6543",
            dbname="postgres",
            user="postgres.uahaoubommqaqkqslgjj",
            password="God303!John."
        )
        cursor = conn.cursor()
        # Evitar SQL injection com parâmetros em vez de interpolação direta
        query = "SELECT ai.senha FROM public.admin_imob ai WHERE username=%s"
        cursor.execute(query, (usuario,))
        psw = cursor.fetchone()
        conn.close()

        if psw and psw[0] == senha:
            return usuario
        else:
            return None
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
        return None

# Página de login
def login_page():
    st.title("Login")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        logar = st.button("Entrar")
    if logar:
        user = validar_login(usuario, senha)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = user
            st.success("Login bem-sucedido!")
            st.rerun()  # Força a atualização da página
        else:
            st.error("Usuário ou senha incorretos.")

# Verifica se o usuário está logado
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_page()
else:
    # Se o usuário estiver logado, mostrar a navegação
    principal = st.Page("principal.py", title="J Imobil", icon=":material/dashboard:", default=True)
    empreendimentos = st.Page("jimob/empreendimento.py", title="Empreendimento", icon=":material/dashboard:")

    pg = st.navigation(
        {"Principal": [principal],
        "Empreendimentos": [empreendimentos]}
    )

    # Botão para fazer logout
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()  # Força a atualização da página

    # Rodar a página
    pg.run()
