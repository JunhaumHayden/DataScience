# 📊 Relatório de Análise de Vendas - Seu João Store

Este relatório apresenta os principais resultados obtidos com base na análise dos dados das quatro lojas do Sr. João, com foco em faturamento, desempenho por categoria, satisfação do cliente e logística de entrega.

---

## 1. 🏪 Faturamento Geral e por Ano

As lojas obtiveram os seguintes faturamentos acumulados no período analisado:

![Faturamento por Loja e Ano](../assets/img/faturamento_total_x_loja.png)

A Loja 1 lidera o faturamento total, embora tenha apresentado uma **queda constante** ao longo dos anos:

![Faturamento por Loja e Ano](../assets/img/Faturamento_Anual_Loja.png)

---

## 2. 📦 Vendas por Categoria de Produto

Os produtos mais vendidos por categoria foram:

![Vendas por Categoria](../assets/img/vendas_por_categoria.png)
E detalhando por loja tem-se que eletrônicos e eletrodomésticos foram os mais vendidos em todas as lojas, com destaque para a Loja 1:

![Vendas por Categoria](../assets/img/vendas_categoria_por_loja.png)

### Produtos mais vendidos (Top 10):
O produtos mais vendidos foram:
![top 10 mais vendidos](../assets/img/top10_produtos_geral.png)


## 3. 🌟 Avaliação dos Clientes

A média de avaliações recebidas pelas lojas foi:

![Avaliações por loja](../assets/img/Avaliacao_Media_Loja.png)

Apesar de liderar em faturamento, a Loja 1 tem a **pior avaliação média**.  
A dispersão das notas mostra outliers e variações relevantes:

![Dispersão das Avaliações](../assets/img/boxplot_avaliacoes_loja.png)

---

## 4. 💳 Ticket Médio

O valor médio gasto por cliente em cada loja foi:

![Ticket médio](../assets/img/Ticket_Medio_Loja.png)

Isso indica que a **Loja 1 tem maior faturamento por compra**, o que justifica em parte sua liderança no total.

---

## 5. 🚚 Frete

Analisamos o custo médio do frete por loja:

![Frete Médio](../assets/img/frete_medio_por_loja.png)

E por tipo de pagamento:

![Frete Médio](../assets/img/frete_por_tipo_pagamento.png)

A **Loja 4** se destaca com o **frete mais barato**, e os **clientes que usam cartão de débito pagam menos frete**, em média.

---

### 🔍 Análise Cruzada
- 📈 Loja 1: Maior faturamento, mas pior avaliação média. Pode estar vendendo bem no curto prazo, mas clientes saem menos satisfeitos.
- 🟨 Loja 2: Faturamento estável, avaliação média boa — regular em tudo.
- 🟩 Loja 3: Melhor avaliação de todas, com faturamento competitivo. Alta satisfação e bom desempenho financeiro.
- 🟥 Loja 4: Menor faturamento e avaliação mais fraca que as demais (exceto Loja 1). Pode estar com menor fluxo de vendas e não encantando os clientes.

### ✅ Recomendação Final
O Senhor João deve considerar vender a Loja 1.

Por quê?

- Apesar de liderar o faturamento, a Loja 1 tem a pior avaliação média. Isso pode indicar clientes insatisfeitos mesmo com alto volume de vendas — o que prejudica a reputação da rede e pode gerar queda futura.
- É o momento ideal de vender enquanto os números ainda são altos, aproveitando o valor de mercado.

Alternativamente:

Se o objetivo for vender uma operação menos estratégica e menos lucrativa, a Loja 4 também é candidata, pois tem:
- O menor faturamento.
- Uma avaliação média apenas ok — não fideliza como as demais.

### 📌 Outras Recomendações
- Melhorar a **avaliação da Loja 1**, talvez com foco no atendimento ou logística.
- Investir em categorias com alta demanda, como **eletrônicos e eletrodomésticos**.
- Monitorar o **frete** para reduzir custos e evitar impactos nas notas.
- Explorar promoções nos **produtos mais vendidos** para alavancar ainda mais o volume de vendas.

---

Relatório gerado automaticamente via Jupyter Notebook.  
Imagens atualizados em: `assets/img`  


