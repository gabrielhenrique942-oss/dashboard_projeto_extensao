import pandas as pd

def carregar_dados():
    return pd.read_csv("data/dados_ans.csv")

def tratar_dados(df):
    df.columns = df.columns.str.lower().str.strip()
    df = df.dropna()
    return df

def gerar_metricas(df):
    df["sinistralidade"] = df["despesa_assistencial"] / df["receita"]
    df["margem"] = df["receita"] - df["despesa_assistencial"]
    df["custo_medio"] = df["despesa_assistencial"] / df["beneficiarios"]
    return df

def pipeline():
    df = carregar_dados()
    df = tratar_dados(df)
    df = gerar_metricas(df)
    return df