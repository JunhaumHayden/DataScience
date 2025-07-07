<div align="center">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Logo Python" width="110">
</div>
<h1 align="center"> Data Analysis </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

![Made by Hayden](https://img.shields.io/badge/Made-_by_Hayden-0d1117?style=for-the-badge)

![Powered by Python](https://img.shields.io/badge/Powered_by-Python-3776AB?logo=python&logoColor=white)
![Powered by Pandas](https://img.shields.io/badge/Powered_by-Pandas-150458?logo=pandas&logoColor=white)
![Powered by Matplotlib](https://img.shields.io/badge/Powered_by-Matplotlib-11557C?logo=matplotlib&logoColor=white)
![Powered by Jupyter](https://img.shields.io/badge/Powered_by-Jupyter-F37626?logo=jupyter&logoColor=white)



# 🧓📊 Seu João Store - Qual loja vender?

Seja bem-vindo(a) ao projeto **Seu João Store**!  
Aqui ajudamos o querido Senhor João — que jurava que Excel era o nome de um remédio — a descobrir qual loja da sua rede fictícia *Alura Store* ele deveria vender para investir em um novo empreendimento.  
Spoiler: o coração dizia uma, os dados disseram outra. 📉💔

## 🎯 Propósito da Análise

O objetivo deste projeto é analisar dados de desempenho, faturamento e avaliações de **4 lojas fictícias** da *Alura Store* e recomendar qual delas tem a **menor eficiência**, ou seja, qual o Senhor João deveria vender para maximizar suas chances de sucesso no novo negócio.

Durante a análise, buscamos responder:

- Qual loja fatura menos?
- Quais têm os menores índices de satisfação do cliente?
- Quais produtos e categorias têm melhor (ou pior) desempenho?
- Onde o frete é um pesadelo logístico?

## 📁 Estrutura do Projeto

```bash
seu-jose-store-analysis/
├── data/  ## dados de entrada
│   ├── loja1.csv
│   ├── loja2.csv
│   ├── loja3.csv
│   └── loja4.csv
│
├── assets/
│   ├── img/   # imagens geradas durante a análise
|
├── notebooks/
│   └── analise_lojas.ipynb      # Notebook principal com toda a lógica e visualizações
│
├── reports/
│   └── recomendacao_final.md    # Texto final da análise/recomendação
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py           # Leitura dos dados CSV
│   ├── visualizations.py        # Geração de gráficos
│   ├── analysis.py              # Lógica de análise e métricas
│   └── utils.py                 # Funções auxiliares (se necessário)
│
├── requirements.txt
├── README.md      # Este arquivo lindão aqui
└── .gitignore
                    
```

##📊 Exemplos de Gráficos e Insights

### 💸 Faturamento por loja 
- - Insight: A Loja C apresentou o menor faturamento, com uma diferença considerável em relação às demais. 
### ⭐ Média de Avaliações
- - Insight: A Loja B possui as piores avaliações, o que pode indicar problemas de atendimento, produto ou entrega.
### 📦 Categorias mais vendidas por loja
- - Insight: A Loja D é altamente dependente de uma única categoria de produtos, o que pode ser um risco no longo prazo.

## ✅ Recomendação Final

Após análise dos dados de faturamento, avaliação dos clientes, número de vendas, categorias e custo médio de frete, recomendamos que o Senhor João venda a Loja C.
Apesar de não ter a pior avaliação, ela apresenta baixa performance geral, com menor faturamento, dependência de poucos produtos e baixo volume de vendas.
Em outras palavras, se fosse um personagem em um RPG, a Loja C seria o NPC que não ajuda nem atrapalha. Hora de deixá-la ir. 🪦📉

## ⚙️ Como Executar o Notebook

Para rodar este projeto no seu ambiente local, siga os passos abaixo:

1. lone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-jose-store.git
cd seu-jose-store
```
2. Instale as dependências (recomenda-se o uso de um ambiente virtual):
```
pip install pandas matplotlib jupyter
```
3. Inicie o Jupyter Notebook:
```bash
jupyter notebook
```
4. Abra o arquivo `Seu_Jose_Store_Analise.ipynb` e execute as células.

## 💡 Tecnologias Utilizadas

- Python 🐍
- Pandas 📑
- Matplotlib 📊
- Jupyter Notebook 📘

# Author


Este projeto foi desenvolvido por Carlos Hayden — um entusiasta de dados, apaixonado por transformar tabelas em decisões inteligentes.

Se quiser conversar, dar dicas ou mandar gifs de gatinhos com gráficos, me enviar uma issue️.

"Confie nos dados, não nas intuições... a menos que você seja o Mestre Yoda."

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |