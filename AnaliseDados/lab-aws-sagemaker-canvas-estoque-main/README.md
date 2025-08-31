# 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

Bem-vindo ao projeto "Previsão de Estoque Inteligente na AWS com SageMaker Canvas". Neste Lab usando o SageMaker Canvas para criar previsões de estoque baseadas em Machine Learning (ML). 

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter uma conta na AWS. 
[AWS Cloud Quickstart](https://github.com/digitalinnovationone/aws-cloud-quickstart).


## 🎯 Objetivos Deste Projeto (Lab)

![image](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque/assets/730492/72f5c21f-5562-491e-aa42-2885a3184650)

## Previsão de Estoque Inteligente

### Introdução

Este repositório contém o projeto de previsão de estoque utilizando Machine Learning no-code via Amazon SageMaker Canvas. O objetivo é prever a quantidade de estoque disponível para diferentes produtos, considerando variáveis como preço e promoções.

### Passo a Passo

1. Seleção do Dataset
O dataset utilizado foi importado no Amazon SageMaker Canvas e contém as seguintes colunas:

ID_PRODUTO: Identificação do produto.
DATA_EVENTO: Data do evento.
PRECO: Preço do produto.
FLAG_PROMOCAO: Indica se o produto está em promoção (1) ou não (0).
QUANTIDADE_ESTOQUE: Quantidade de estoque disponível.
Exemplo do dataset:

``` csv
Copy code
ID_PRODUTO,DATA_EVENTO,PRECO,FLAG_PROMOCAO,QUANTIDADE_ESTOQUE
1000,2023-12-31,138.43,1,100
1001,2023-12-31,75.08,0,100
1002,2023-12-31,58.84,0,100
1003,2023-12-31,61.96,0,100
1004,2023-12-31,20.34,0,100
...
``` 

2. Preparação dos Dados
Após a importação, os dados foram preparados para o treinamento do modelo. Isso incluiu a verificação de valores nulos, a conversão de tipos de dados e a normalização de valores.

3. Treinamento do Modelo
Utilizando a interface no-code do SageMaker Canvas, foi possível configurar e treinar o modelo de Machine Learning. O modelo foi treinado para prever a QUANTIDADE_ESTOQUE com base nas outras variáveis do dataset.

4. Avaliação do Modelo
O modelo foi avaliado utilizando métricas de performance disponíveis no SageMaker Canvas, como RMSE (Root Mean Squared Error) e R² (Coeficiente de Determinação). As métricas indicaram a acurácia das previsões do modelo.

5. Implementação e Previsões
Após a validação, o modelo foi implementado para realizar previsões sobre novos dados de estoque. As previsões ajudaram a entender a demanda futura e ajustar o estoque de maneira eficiente.

### Conclusões

A utilização do Amazon SageMaker Canvas para criar um modelo de previsão de estoque demonstrou ser eficiente e prática. A ferramenta no-code facilitou o processo de preparação, treinamento e implementação do modelo de Machine Learning, permitindo que insights valiosos fossem obtidos rapidamente.

#### As principais conclusões foram:

A promoção dos produtos (indicada pela FLAG_PROMOCAO) tem um impacto significativo na quantidade de estoque.
A variação de preço também influencia a quantidade de estoque disponível.
Modelos de Machine Learning no-code são viáveis para cenários de previsão de estoque, oferecendo facilidade e rapidez na implementação.


## 🚀 Passo a Passo no Sagemaker Canvas

### 1. Selecionar Dataset

-   Navegue até a pasta `datasets` deste repositório. Esta pasta contém os datasets que você poderá escolher para treinar e testar seu modelo de ML. 
-   Escolha o dataset que você usará para treinar seu modelo de previsão de estoque.
-   Faça o upload do dataset no SageMaker Canvas.

### 2. Construir/Treinar

-   No SageMaker Canvas, importe o dataset que você selecionou.
-   Configure as variáveis de entrada e saída de acordo com os dados.
-   Inicie o treinamento do modelo. Isso pode levar algum tempo, dependendo do tamanho do dataset.

### 3. Analisar

-   Após o treinamento, examine as métricas de performance do modelo.
-   Verifique as principais características que influenciam as previsões.
-   Faça ajustes no modelo se necessário e re-treine até obter um desempenho satisfatório.

### 4. Prever

-   Use o modelo treinado para fazer previsões de estoque.
-   Exporte os resultados e analise as previsões geradas.
-   Documente suas conclusões e qualquer insight obtido a partir das previsões.


## Recursos Adicionais
Durante este conteúdo, abordou-se diversos aspectos do SageMaker Canvas e como ele permite a criação de modelos de Machine Learning (ML) de forma intuitiva, sem necessidade de programação. Para aprofundar o conhecimento, segue alguns materiais complementares específicos:

- [Documentação Oficial do SageMaker Canvas](https://aws.amazon.com/sagemaker/canvas/): Consulte a página oficial da AWS para obter detalhes técnicos, guias de uso e exemplos práticos do SageMaker Canvas.
- [Guia de Introdução ao SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html): Explore o guia de introdução ao Amazon SageMaker, que abrange desde a preparação de dados até a implantação de modelos de ML.
- [Tutoriais e Exemplos Práticos](https://aws.amazon.com/sagemaker/resources/?sagemaker-resources-whats-new.sort-by=item.additionalFields.postDateTime&sagemaker-resources-whats-new.sort-order=desc&ar-cards-sagemaker.sort-by=item.additionalFields.datePublished&ar-cards-sagemaker.sort-order=desc): Acesse a seção de recursos do SageMaker para tutoriais detalhados e exemplos de casos de uso práticos que podem servir como inspiração para seus próprios projetos.
- [Repositório de Exemplo](https://github.com/aws/amazon-sagemaker-examples): Confira este repositório no GitHub que contém exemplos de uso do SageMaker, incluindo scripts e notebooks que você pode adaptar para suas necessidades.