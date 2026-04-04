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
st.write("""
Este Projeto apresenta uma análise atuarial e financeira aplicada ao setor de saúde suplementar brasileiro,
com base em dados da Agência Nacional de Saúde Suplementar (ANS). A proposta consiste em integrar informações
relevantes sobre beneficiários, receitas e despesas assistenciais, permitindo uma leitura estruturada do desempenho
econômico e do nível de risco das operadoras analisadas.

A aplicação foi desenvolvida com o objetivo de apoiar a interpretação de indicadores fundamentais, como
sinistralidade, custo médio por beneficiário e margem operacional, os quais são amplamente utilizados no
contexto atuarial para avaliação da sustentabilidade financeira e do equilíbrio técnico das carteiras de saúde.

Além disso, o Projeto incorpora elementos analíticos que possibilitam identificar padrões e relações entre
variáveis-chave, contribuindo para uma compreensão mais aprofundada do comportamento dos custos assistenciais e
dos desafios associados à gestão de risco no setor. A inclusão de uma pirâmide etária, ainda que em caráter
ilustrativo, reforça a dimensão social da análise, evidenciando o impacto da estrutura demográfica sobre a demanda
por serviços de saúde.

Dessa forma, a ferramenta proposta oferece suporte à análise crítica e à tomada de decisão, integrando conceitos
atuariais e financeiros em uma interface interativa, clara e orientada à interpretação de dados.
""")
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

# Ordenação para melhor leitura
df = df.sort_values("sinistralidade", ascending=False)

# Visualizações
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

# Pirâmide etária
st.subheader("Pirâmide Etária")
st.plotly_chart(grafico_piramide_etaria(), use_container_width=True)
st.caption(
    "A pirâmide etária representa, de forma ilustrativa, a distribuição populacional por faixas de idade e sexo. "
    "No contexto atuarial, estruturas etárias mais envelhecidas tendem a estar associadas a maior utilização de "
    "serviços assistenciais e maior pressão sobre custos."
)

# Ranking
st.subheader("Ranking de Sinistralidade")
st.dataframe(df[["operadora", "sinistralidade"]], use_container_width=True)

# Análise final
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

A inclusão da pirâmide etária reforça a perspectiva social e atuarial do dashboard, ao destacar
como a composição etária da população pode influenciar a demanda por serviços de saúde e o comportamento
dos custos assistenciais no longo prazo.

Dessa forma, o dashboard organiza informações relevantes para a interpretação atuarial e financeira
do setor, oferecendo apoio à análise de risco, ao acompanhamento da sustentabilidade e à compreensão
do equilíbrio entre crescimento da carteira, arrecadação e custos assistenciais.
""")