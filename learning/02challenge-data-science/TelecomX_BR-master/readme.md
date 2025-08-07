# Análise de Churn de Clientes - TelecomX

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-orange?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-red?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-purple?style=flat&logo=seaborn)

## 📄 Descrição do Projeto

Este repositório contém uma análise exploratória de dados (EDA) focada na identificação dos principais fatores que levam clientes da **TelecomX** a cancelar seus serviços (Churn). O objetivo é transformar dados brutos em insights acionáveis que a empresa possa usar para desenvolver estratégias eficazes de retenção de clientes, reduzir perdas de receita e otimizar custos de aquisição.

O problema do Churn é crítico para empresas de serviços por assinatura, impactando diretamente a receita recorrente, os custos de aquisição de novos clientes e a reputação da marca. Esta análise busca mitigar esses riscos através de um entendimento aprofundado dos padrões de evasão.

O projeto foi desenvolvido como parte de um curso de Challenge Telecom X: Análise de Evasão de Clientes da Alura em parceria com a Oracle Next Education.

## 🚀 Como Executar o Projeto

Para replicar a análise e os gráficos gerados neste projeto, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina (versão 3.9 ou superior é recomendada).

### Dependências

As bibliotecas Python necessárias para este projeto podem ser instaladas via `pip`. Você pode instalá-las de uma vez usando o comando:

```bash
pip install pandas matplotlib seaborn jupyter
```
- pandas: Para manipulação e análise de dados.

- matplotlib: Para criação de gráficos estáticos.

- seaborn: Para visualizações estatísticas de dados.

- jupyter: Para executar o notebook interativo (.ipynb).

## Estrutura do Repositório
```
TelecomX_BR/
├── TelecomX_BR.ipynb         # O notebook Jupyter com toda a análise
├── TelecomX_data_tratados.json # Conjunto de dados tratado e utilizado na análise
├── TelecomX_Data.json        # Conjunto de dados original (se houver)
├── TelecomX_data_tratados.csv # Conjunto de dados tratado em formato CSV (se houver)
└── readme.md                 # Este arquivo README
```
## Passos para Execução
1. Clone o Repositório: 
- git clone [https://github.com/dfarneym/TelecomX_BR.git](https://github.com/dfarneym/TelecomX_BR.git)
- cd TelecomX_BR

2. Abra o Notebook Jupyter:
```bash
jupyter notebook TelecomX_BR.ipynb
```
3. Execute as Células:
- Dentro do navegador, o ambiente Jupyter será aberto. Execute as células do notebook sequencialmente. O notebook está estruturado para guiar você através das etapas de:

- Limpeza e Tratamento de Dados: Carregamento do TelecomX_Data.json, tratamento de valores ausentes e transformação da variável alvo (Cancelou).

- Análise Exploratória de Dados: Geração e interpretação de gráficos sobre a influência do tipo de contrato, meses de permanência, cobrança mensal e método de pagamento no Churn.

- Conclusões e Recomendações: Resumo dos insights obtidos e sugestões de ações estratégicas.

### 📊Gráficos e Insights

* **Gráfico 1 - Distribuição Geral de Cancelamentos**: Vemos que a base de dados é desbalanceada. Cerca de 26,6% dos clientes cancelaram, enquanto 73,4% permaneceram. Isso nos mostra que a maioria dos clientes é leal, mas há uma parcela significativa que precisa de atenção:

![Distribuição Geral de Cancelamentos](Gráficos/Distribuição%20Geral%20de%20Cancelamentos.png)

* **Gráfico 2 - Proporção de Cancelamento por Tipo de Contrato**:

![Distribuição Geral de Cancelamentos](Gráficos/Proporção%20de%20Cancelamento%20por%20Tipo%20de%20Contrato.png)

- Contrato Mensal: A barra vermelha (Cancelou = Sim) é enorme, mostrando que mais de 42% dos clientes com este tipo de contrato cancelam o serviço.
- Contrato de Um Ano: A taxa de cancelamento cai drasticamente, ficando em torno de 11%.
- Contrato de Dois Anos: É o mais seguro para a empresa, com uma taxa de cancelamento baixíssima, de apenas ~3%.


* **Gráfico 3 - Proporção de Cancelamento por Tipo de Contrato**:

![Relação entre Cobrança Mensal e Cancelamento](Gráficos/Relação%20entre%20Cobrança%20Mensal%20e%20Cancelamento.png)

- Cobrança Mensal (Gráfico 3): O boxplot mostra claramente que os clientes que cancelam (Sim) tendem a ter uma cobrança mensal mediana mais alta (cerca de R$80) em comparação com os que não cancelam (mediana em torno de R$65). Clientes com cobranças muito baixas (abaixo de R$30) raramente cancelam.

* **Gráfico 4 - Relação entre Meses de Permanência e Cancelamento**:

![Relação entre Meses de Permanência e Cancelamento](Gráficos/Relação%20entre%20Meses%20de%20Permanência%20e%20Cancelamento.png)

- Meses de Permanência (Gráfico 4): O histograma revela outro padrão crucial. A maioria dos cancelamentos ocorre nos primeiros meses do serviço. Clientes que superam a marca de um ano tendem a se tornar muito mais leais. A lealdade aumenta com o tempo de permanência.

* **Gráfico 5 -  Proporção de Cancelamento por Fatores Demográficos**:
![ Proporção de Cancelamento por Fatores Demográficos ](Gráficos/Proporção%20de%20Cancelamento%20por%20Fatores%20Demográficos.png)

- Gênero: A taxa de cancelamento é praticamente idêntica para os gêneros Feminino (26,9%) e Masculino (26,2%). Isso nos mostra que o gênero não é um fator relevante para prever o cancelamento.

- Cliente Idoso: Aqui a diferença é gritante. Clientes idosos (Sim) cancelam numa proporção muito maior (41,7%) do que os clientes não idosos (Não), que têm uma taxa de apenas 23,6%. Ser idoso é um forte indicador de risco de cancelamento.

- Possui Cônjuge: Clientes sem cônjuge (Não) têm uma taxa de cancelamento maior (33,0%) em comparação com aqueles que possuem um parceiro (Sim), cuja taxa é de 19,7%.

- Possui Dependentes: O padrão é semelhante ao do cônjuge. Clientes sem dependentes (Não) cancelam muito mais (31,3%) do que aqueles que possuem dependentes (Sim), que têm uma taxa de apenas 15,5%.

# 💡 Insights e Conclusões Principais
- A análise revelou um perfil claro do cliente com alto risco de Churn:

- Contrato Mensal: Clientes com esse tipo de contrato apresentam as maiores taxas de cancelamento.

- Baixo Tempo de Permanência: A maioria dos cancelamentos ocorre nos primeiros meses de serviço.

- Cobrança Mensal Elevada: Clientes com contas mais altas têm maior propensão a cancelar.

- Método de Pagamento "Cheque Eletrônico": Associado a uma taxa de Churn significativamente superior.

- Perfil Demográfico Específico: Clientes idosos e que não possuem dependentes ou cônjuge também mostraram maior propensão ao Churn.

- Ausência de Serviços Adicionais: Clientes que não contratam serviços de valor agregado (ex: Segurança Online, Suporte Técnico) tendem a cancelar mais.

## 📈 Futuras Análises e Próximas Ações e Melhorias
Com base nos insights, as seguintes recomendações são sugeridas para a TelecomX:

Campanhas de Migração de Contrato: Incentivar clientes de planos mensais a migrarem para contratos de maior duração (1 ou 2 anos) com ofertas atrativas.

1. Programa de Onboarding e Engajamento Inicial: Desenvolver um acompanhamento dedicado para novos clientes nos primeiros 3 a 6 meses para garantir uma experiência positiva e fortalecer o relacionamento.

2. Ações de Retenção para Clientes de Alto Valor: Monitorar e engajar proativamente clientes com faturas mensais elevadas, oferecendo revisões de plano ou benefícios de fidelidade.

3. Revisão do Método de Pagamento "Cheque Eletrônico": Investigar as causas da alta taxa de Churn associada a este método e buscar soluções ou incentivar a migração para métodos mais estáveis (débito automático, cartão de crédito).

4. Atenção e Adaptação para o Público Idoso: Avaliar a usabilidade dos serviços e a qualidade do suporte técnico para esse segmento, buscando canais de comunicação simplificados e atendimento mais paciente.
