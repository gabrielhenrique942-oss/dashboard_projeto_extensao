import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def grafico_receita_despesa(df):
    return px.bar(
        df,
        x="operadora",
        y=["receita", "despesa_assistencial"],
        barmode="group",
        title="Receita vs Despesa Assistencial"
    )


def grafico_margem(df):
    return px.bar(
        df,
        x="operadora",
        y="margem",
        title="Margem Operacional"
    )


def grafico_beneficiarios(df):
    return px.scatter(
        df,
        x="beneficiarios",
        y="receita",
        title="Beneficiários vs Receita"
    )


def grafico_custo(df):
    return px.bar(
        df,
        x="operadora",
        y="custo_medio",
        title="Custo Médio por Beneficiário"
    )


def grafico_sinistralidade(df):
    return px.bar(
        df,
        x="operadora",
        y="sinistralidade",
        title="Sinistralidade por Operadora"
    )


def grafico_piramide_etaria():
    # Dados simulados para complementar a análise atuarial
    dados = {
        "faixa_etaria": ["0-18", "19-30", "31-45", "46-60", "60+"],
        "masculino": [-20000, -30000, -25000, -18000, -12000],
        "feminino": [22000, 32000, 27000, 20000, 15000]
    }

    df = pd.DataFrame(dados)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=df["faixa_etaria"],
            x=df["masculino"],
            name="Masculino",
            orientation="h"
        )
    )

    fig.add_trace(
        go.Bar(
            y=df["faixa_etaria"],
            x=df["feminino"],
            name="Feminino",
            orientation="h"
        )
    )

    fig.update_layout(
        title="Pirâmide Etária (Simulação)",
        barmode="relative",
        xaxis_title="Quantidade",
        yaxis_title="Faixa Etária"
    )

    return fig