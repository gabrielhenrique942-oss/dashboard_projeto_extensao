import plotly.express as px

def grafico_receita_despesa(df):
    return px.bar(df, x="operadora", y=["receita", "despesa_assistencial"],
                  barmode="group", title="Receita vs Despesa")

def grafico_margem(df):
    return px.bar(df, x="operadora", y="margem",
                  title="Margem Operacional")

def grafico_beneficiarios(df):
    return px.scatter(df, x="beneficiarios", y="receita",
                      title="Beneficiários vs Receita")

def grafico_custo(df):
    return px.bar(df, x="operadora", y="custo_medio",
                  title="Custo Médio por Beneficiário")

def grafico_sinistralidade(df):
    return px.bar(df, x="operadora", y="sinistralidade",
                  title="Sinistralidade por Operadora")