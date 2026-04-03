def resumo_atuarial(df):
    return {
        "sinistralidade_media": df["sinistralidade"].mean(),
        "custo_medio": df["custo_medio"].mean(),
        "receita_media": df["receita"].mean()
    }