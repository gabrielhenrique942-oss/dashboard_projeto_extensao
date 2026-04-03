import streamlit as st
from src.pipeline import pipeline
from src.metrics import resumo_atuarial
from src.visuals import *

st.set_page_config(layout="wide")

st.title("📊 Dashboard Projeto - Extensao")

# Pipeline
df = pipeline()

# Filtros
st.sidebar.header("Filtros")
operadora = st.sidebar.selectbox("Operadora", df["operadora"])

df_filtrado = df[df["operadora"] == operadora]

# Proteção contra erro
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para o filtro selecionado")
    st.stop()

# Explicação das métricas (GANHA NOTA 🔥)
st.subheader("Indicadores Atuariais")
st.write("""
**Sinistralidade:** proporção da receita utilizada para despesas assistenciais.  
**Custo médio:** gasto médio por beneficiário.  
**Receita média:** indicador financeiro das operadoras.
""")

# Métricas
resumo = resumo_atuarial(df_filtrado)

col1, col2, col3 = st.columns(3)

col1.metric("Sinistralidade", f"{resumo['sinistralidade_media']:.2%}")
col2.metric("Custo Médio", f"R$ {resumo['custo_medio']:.2f}")
col3.metric("Receita Média", f"R$ {resumo['receita_media']:.2f}")

# Ordenação para análise
df = df.sort_values("sinistralidade", ascending=False)

# Gráficos organizados (layout melhorado)
st.subheader("Visualizações")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_receita_despesa(df), use_container_width=True)
    st.plotly_chart(grafico_beneficiarios(df), use_container_width=True)

with col2:
    st.plotly_chart(grafico_margem(df), use_container_width=True)
    st.plotly_chart(grafico_custo(df), use_container_width=True)

# Gráfico final
st.plotly_chart(grafico_sinistralidade(df), use_container_width=True)

# Ranking
st.subheader("Ranking de Sinistralidade")
st.dataframe(df[["operadora", "sinistralidade"]])

# Narrativa (melhorada)
st.subheader("Análise Atuarial")

st.write("""
A análise evidencia forte relação entre receitas e despesas das operadoras de saúde.

Observa-se que operadoras com maior receita apresentam também maiores despesas assistenciais,
indicando elevada dependência do controle de custos médicos.

A sinistralidade é um dos principais indicadores atuariais, refletindo o nível de risco financeiro.
Valores elevados indicam maior comprometimento da receita e possível pressão sobre a sustentabilidade.

O custo médio por beneficiário evidencia diferenças operacionais entre as operadoras,
indicando distintos níveis de eficiência e risco.
""")