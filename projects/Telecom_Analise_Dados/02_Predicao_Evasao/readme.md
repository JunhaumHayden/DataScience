<h1 align="center"> Projeto de Previsão de Evasão de Clientes </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=%20Done&color=GREEN&style=for-the-badge"/>
</p>

---
<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python">
  </a>
  <a href="https://jupyter.org/">
    <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter">
  </a>
  <a href="https://pandas.pydata.org/">
    <img alt="Pandas" src="https://img.shields.io/badge/Pandas-1.5%2B-lightgrey?logo=pandas">
  </a>
  <a href="https://scikit-learn.org/">
    <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-1.1%2B-F7931E?logo=scikit-learn">
  </a>
  <a href="https://seaborn.pydata.org/">
    <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-0.11%2B-lightblue?logo=python">
  </a>
  <a href="https://matplotlib.org/">
    <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-3.5%2B-darkgreen?logo=python">
  </a>
  <a href="https://imbalanced-learn.org/">
    <img alt="imbalanced-learn" src="https://img.shields.io/badge/imblearn-SMOTE-red">
  </a>
  <a href="https://opensource.org/license/mit/">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
  </a>
</p>

[![GitHub Repo stars](https://img.shields.io/github/stars/HaydenUFSC/03_challenge-data-science?style=social)](https://github.com/HaydenUFSC/03_challenge-data-science)
[![GitHub forks](https://img.shields.io/github/forks/HaydenUFSC/03_challenge-data-science?style=social)](https://github.com/HaydenUFSC/03_challenge-data-science/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/HaydenUFSC/03_challenge-data-science?style=social)](https://github.com/HaydenUFSC/03_challenge-data-science/watchers)



Este projeto tem como objetivo identificar os principais fatores que influenciam a evasão de clientes (churn) e propor estratégias de retenção com base em modelos de machine learning.

## 📊 Modelos Utilizados

Foram aplicados dois modelos principais:

- **Regressão Logística**: interpretável e eficaz para prever evasões com alta sensibilidade.
- **Random Forest**: robusto, com bom desempenho em termos de acurácia e precisão.

### Desempenho dos Modelos

| Métrica      | Regressão Logística | Random Forest | Melhor |
| ------------ | ------------------- | ------------- | ------ |
| Acurácia     | 0.74                | **0.77**      | RF     |
| Precisão (1) | 0.50                | **0.57**      | RF     |
| Recall (1)   | **0.80**            | 0.56          | RL     |
| F1-score (1) | **0.62**            | 0.57          | RL     |
| ROC AUC      | **0.83**            | 0.81          | RL     |

## 🔍 Conclusão Técnica

- **Regressão Logística** teve melhor desempenho na identificação de clientes que evadem, além de ser mais interpretável.
- **Random Forest** obteve melhor acurácia geral, sendo mais robusto para ambientes com dados complexos.

| Objetivo do Negócio                             | Modelo Recomendado      |
|--------------------------------------------------|--------------------------|
| Detectar o maior número de clientes que evadem   | Regressão Logística      |
| Equilibrar performance geral e robustez          | Random Forest            |
| Explicar decisões com base em variáveis preditoras | Regressão Logística    |

## 🎯 Conclusão Estratégica

A evasão está fortemente ligada a:

- Contratos mensais.
- Baixo tempo de permanência.
- Baixo valor acumulado em faturas.

### ✅ Estratégias Recomendadas

- Incentivar contratos mais longos com benefícios.
- Ações personalizadas nas primeiras semanas de adesão.
- Monitorar clientes com baixa fatura e engajamento.
- Criar campanhas de fidelização baseadas no perfil dos clientes mais fiéis.

## 🔚 Insight Final

A Regressão Logística se destaca como o modelo mais eficaz para antecipar evasões com base em fatores interpretáveis. O Random Forest complementa com robustez e bom desempenho geral. A combinação de ambos pode potencializar os resultados das estratégias de retenção.

---



🧠 Licença

MIT — ou seja: use, quebre, refaça, mas me cite se for ficar famoso com isso 😎




---
# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |

© 2025 - Projeto de Análise de Evasão de Clientes