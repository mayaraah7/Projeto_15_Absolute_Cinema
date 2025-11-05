import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Top Filmes IMDb",
    page_icon="🎬",
    layout="wide"
)

# Carregar dados dos filmes
filmes = pd.read_csv("filmes.csv")

# Sidebar apenas com filtro de gênero
st.sidebar.title("Mayarah Play")
st.sidebar.image("logo.png")
st.sidebar.title("filtros")
genero_escolhido = st.sidebar.selectbox(
    "filtrar por genero:",
    ["Todos"]+sorted(filmes["Genre"].unique().tolist())
)

# Aplicar filtro
if genero_escolhido == "Todos":
    filmes_filtrados = filmes
else:
    filmes_filtrados = filmes[filmes["Genre"]==genero_escolhido]

# Título da página
st.title("May Movies")
# Mostrar quantidade de filmes
st.write(f"**{len(filmes_filtrados)}filmes filtrados**")

# Mostrar filmes em grid (3 colunas)
colunas = st.columns(3)

for index, filme in filmes_filtrados.iterrows():
    # Calcular em qual coluna colocar (0, 1 ou 2)
    coluna_index = index % 3
    
    with colunas[coluna_index]:
        # Container de cada filme com altura fixa
        with st.container():
            # Imagem com altura fixa
            st.image(filme['Image URL'], use_container_width=True)
            
            # Informações do filme
            st.subheader(f"#{filme['Rank']}-{filme["Title"]}")
            st.write(f"**Ano:**{filme["Year"]}")
            st.write(f"**⭐ Nota:** {filme['Rating']}")
            st.write(f"**⏱️ Duração:** {filme['Duration']}")
            st.write(f"**🎭 Gênero:** {filme['Genre']}")
                    
            
            # Botão para ver no IMDb
            if st.button(f"Ver no IMDb", key=f"btn_{filme['Rank']}"):
                st.markdown(f"[🔗 Abrir página do IMDb]({filme['IMDb URL']})")
            
       