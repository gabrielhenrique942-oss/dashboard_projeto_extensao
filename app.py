import streamlit as st
from src.pipeline import pipeline
from src.metrics import resumo_atuarial
from src.visuals import *

st.set_page_config(layout="wide")

st.title("📊 Dashboard Projeto - Extensao")

st.write("""
Este dashboard apresenta uma análise atuarial e financeira com base em dados do setor de saúde suplementar,
utilizando informações da Agência Nacional de Saúde Suplementar (ANS). A aplicação foi estruturada para
permitir a visualização de indicadores relevantes, apoiar a interpretação dos resultados e facilitar a
compreensão das relações entre beneficiários, receitas, despesas assistenciais e sustentabilidade operacional
das operadoras analisadas.
""")

# Pipeline
df = pipeline()

# Filtros
st.sidebar.header("Filtros")
operadora = st.sidebar.selectbox("Operadora", df["operadora"])

df_filtrado = df[df["operadora"] == operadora]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para o filtro selecionado.")
    st.stop()

# Métricas
st.subheader("Indicadores Atuariais")
st.write("""
**Sinistralidade:** proporção da receita utilizada para despesas assistenciais.  
**Custo médio:** gasto médio por beneficiário.  
**Receita média:** indicador financeiro das operadoras.
""")

resumo = resumo_atuarial(df_filtrado)

col1, col2, col3 = st.columns(3)
col1.metric("Sinistralidade", f"{resumo['sinistralidade_media']:.2%}")
col2.metric("Custo Médio", f"R$ {resumo['custo_medio']:.2f}")
col3.metric("Receita Média", f"R$ {resumo['receita_media']:.2f}")

df = df.sort_values("sinistralidade", ascending=False)

st.subheader("Visualizações")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_receita_despesa(df), use_container_width=True)
    st.caption(
        "O gráfico compara receitas e despesas assistenciais das operadoras, permitindo observar o volume "
        "financeiro movimentado e o grau de comprometimento das receitas com custos assistenciais."
    )

    st.plotly_chart(grafico_beneficiarios(df), use_container_width=True)
    st.caption(
        "A relação entre beneficiários e receita evidencia como o tamanho da carteira influencia o faturamento, "
        "sugerindo associação positiva entre expansão da base e crescimento financeiro."
    )

with col2:
    st.plotly_chart(grafico_margem(df), use_container_width=True)
    st.caption(
        "A margem operacional mostra a diferença entre receita e despesa assistencial, contribuindo para avaliar "
        "a capacidade de geração de resultado das operadoras."
    )

    st.plotly_chart(grafico_custo(df), use_container_width=True)
    st.caption(
        "O custo médio por beneficiário permite comparar diferenças de eficiência operacional e intensidade de gastos "
        "entre as operadoras analisadas."
    )

st.plotly_chart(grafico_sinistralidade(df), use_container_width=True)
st.caption(
    "A sinistralidade sintetiza o grau de comprometimento da receita com despesas assistenciais, sendo um dos "
    "principais indicadores de risco e sustentabilidade no contexto atuarial."
)

# Ranking
st.subheader("Ranking de Sinistralidade")
st.dataframe(df[["operadora", "sinistralidade"]])

# Narrativa analítica
st.subheader("Análise Atuarial e Financeira")

st.write("""
A análise dos dados da Agência Nacional de Saúde Suplementar (ANS) permite observar a relação
entre beneficiários, receitas e despesas assistenciais das operadoras avaliadas.

Os resultados indicam que operadoras com maior volume de receita também apresentam despesas
assistenciais mais elevadas, o que evidencia a necessidade de monitoramento contínuo da eficiência
operacional e do controle de custos no setor de saúde suplementar.

A sinistralidade representa um dos principais indicadores atuariais desta análise, pois expressa
o grau de comprometimento da receita com despesas assistenciais. Valores mais altos podem sinalizar
maior pressão financeira e menor folga operacional, afetando a sustentabilidade das operadoras.

O custo médio por beneficiário complementa essa avaliação ao permitir comparar diferenças de
eficiência entre as operadoras. Já a margem operacional contribui para identificar a capacidade
de geração de resultado após a cobertura das despesas assistenciais.

Dessa forma, o dashboard organiza informações relevantes para a interpretação atuarial e financeira
do setor, oferecendo apoio à análise de risco, ao acompanhamento da sustentabilidade e à compreensão
do equilíbrio entre crescimento da carteira, arrecadação e custos assistenciais.
""")