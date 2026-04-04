import streamlit as st
from src.pipeline import pipeline
from src.metrics import resumo_atuarial
from src.visuals import (
    grafico_receita_despesa,
    grafico_margem,
    grafico_beneficiarios,
    grafico_custo,
    grafico_sinistralidade,
    grafico_piramide_etaria
)

st.set_page_config(page_title="Projeto de Extensão", layout="wide")

st.title("📊 Projeto de Extensão")

st.write("""
Este dashboard apresenta uma análise atuarial e financeira aplicada ao setor de saúde suplementar brasileiro,
com base em dados da Agência Nacional de Saúde Suplementar (ANS). A proposta consiste em integrar informações
relevantes sobre beneficiários, receitas e despesas assistenciais, permitindo uma leitura estruturada do desempenho
econômico e do nível de risco das operadoras analisadas.

A aplicação foi desenvolvida com o objetivo de apoiar a interpretação de indicadores fundamentais, como
sinistralidade, custo médio por beneficiário e margem operacional, os quais são amplamente utilizados no
contexto atuarial para avaliação da sustentabilidade financeira e do equilíbrio técnico das carteiras de saúde.

Além disso, o dashboard incorpora elementos analíticos que possibilitam identificar padrões e relações entre
variáveis-chave, contribuindo para uma compreensão mais aprofundada do comportamento dos custos assistenciais e
dos desafios associados à gestão de risco no setor. A inclusão de uma pirâmide etária, ainda que em caráter
ilustrativo, reforça a dimensão social da análise, evidenciando o impacto da estrutura demográfica sobre a demanda
por serviços de saúde.

Dessa forma, a ferramenta proposta oferece suporte à análise crítica e à tomada de decisão, integrando conceitos
atuariais e financeiros em uma interface interativa, clara e orientada à interpretação de dados.
""")

# Carregamento dos dados
df = pipeline()

# Filtros
st.sidebar.header("Filtros")
operadora = st.sidebar.selectbox("Operadora", df["operadora"])

df_filtrado = df[df["operadora"] == operadora]

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para o filtro selecionado.")
    st.stop()

# Indicadores
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

# Ordenação
df = df.sort_values("sinistralidade", ascending=False)

# Visualizações
st.subheader("Visualizações")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_receita_despesa(df), use_container_width=True)
    st.caption(
        "Comparação entre receitas e despesas assistenciais das operadoras, evidenciando o volume financeiro "
        "e o grau de comprometimento das receitas com custos de saúde."
    )

    st.plotly_chart(grafico_beneficiarios(df), use_container_width=True)
    st.caption(
        "Relação entre beneficiários e receita, indicando como o crescimento da carteira impacta o desempenho financeiro."
    )

with col2:
    st.plotly_chart(grafico_margem(df), use_container_width=True)
    st.caption(
        "A margem operacional representa a diferença entre receitas e despesas assistenciais, sendo um indicador "
        "fundamental de sustentabilidade financeira."
    )

    st.plotly_chart(grafico_custo(df), use_container_width=True)
    st.caption(
        "O custo médio por beneficiário permite avaliar a eficiência operacional e comparar níveis de gasto entre operadoras."
    )

st.plotly_chart(grafico_sinistralidade(df), use_container_width=True)
st.caption(
    "A sinistralidade indica o nível de comprometimento da receita com despesas assistenciais, sendo um dos principais "
    "indicadores de risco no contexto atuarial."
)

# Pirâmide etária
st.subheader("Pirâmide Etária")

st.plotly_chart(grafico_piramide_etaria(), use_container_width=True)

st.caption(
    "A pirâmide etária, apresentada de forma ilustrativa, evidencia a distribuição populacional por faixa etária e sexo. "
    "No contexto atuarial, estruturas mais envelhecidas tendem a elevar a utilização de serviços de saúde e os custos assistenciais."
)

# Ranking
st.subheader("Ranking de Sinistralidade")
st.dataframe(df[["operadora", "sinistralidade"]], use_container_width=True)

# Análise final
st.subheader("Análise Atuarial e Financeira")

st.write("""
A análise evidencia que operadoras com maior volume de receita também apresentam maiores despesas assistenciais,
refletindo a necessidade de controle contínuo de custos no setor de saúde suplementar.

A sinistralidade destaca-se como indicador central, pois expressa o grau de comprometimento da receita e permite
avaliar o equilíbrio financeiro das operadoras. Valores elevados podem indicar maior pressão sobre a sustentabilidade.

O custo médio por beneficiário revela diferenças operacionais importantes, enquanto a margem operacional permite
avaliar a capacidade de geração de resultado.

A inclusão da pirâmide etária reforça a análise ao incorporar a dimensão demográfica, essencial para projeções
atuariais e compreensão da evolução dos custos no longo prazo.

Dessa forma, o dashboard integra diferentes perspectivas analíticas, oferecendo suporte à avaliação de risco,
à interpretação de indicadores e à compreensão da dinâmica financeira do setor.
""")