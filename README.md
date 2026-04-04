# 📊 Projeto de Extensão – Análise Atuarial no Setor de Saúde Suplementar

## 📌 Descrição

Este projeto apresenta um dashboard interativo desenvolvido em Python utilizando Streamlit, com foco na análise atuarial e financeira do setor de saúde suplementar brasileiro.

A aplicação integra dados relacionados a beneficiários, receitas e despesas assistenciais, permitindo a visualização e interpretação de indicadores relevantes para avaliação de risco, eficiência operacional e sustentabilidade das operadoras de saúde.

---

## 🎯 Objetivo

O objetivo do projeto é aplicar conceitos atuariais e financeiros na análise de dados reais (ou simulados), proporcionando:

- Avaliação da **sinistralidade**
- Análise do **custo médio por beneficiário**
- Identificação da **margem operacional**
- Interpretação da **sustentabilidade financeira**
- Visualização da **estrutura etária (simulada)**

---

## 📊 Indicadores Utilizados

- **Sinistralidade**: relação entre despesas assistenciais e receita  
- **Custo médio**: despesa média por beneficiário  
- **Margem operacional**: diferença entre receita e despesa  
- **Receita média**: indicador de desempenho financeiro  

---

## 🧠 Contexto Atuarial

A análise atuarial é fundamental para compreender o equilíbrio financeiro das operadoras de saúde.  
Indicadores como sinistralidade e custo médio permitem avaliar o risco associado à carteira de beneficiários.

Além disso, a inclusão da pirâmide etária (simulada) reforça a dimensão social da análise, evidenciando o impacto da estrutura demográfica sobre os custos assistenciais.

---

## 🗂️ Estrutura do Projeto

```text
dashboard_projeto_extensao/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── dados_ans.csv
│
└── src/
    ├── pipeline.py
    ├── metrics.py
    └── visuals.py

    ## Aplicação
(https://dashboardprojetoextensao-ighedjhzajjy3qj4nkxdjb.streamlit.app/)