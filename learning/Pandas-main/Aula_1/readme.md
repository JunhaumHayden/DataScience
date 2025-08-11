Para iniciar uma análise exploratória eficiente de vendas online em um período de 5 dias, depois de extrair a base, vale seguir uma ordem que equilibre entendimento dos dados com identificação de padrões e problemas.

Segue um roteiro estruturado:
1. Compreensão inicial dos dados

    Visualizar estrutura: df.head(), df.tail() e df.sample().

    Dimensões: número de linhas e colunas (df.shape).

    Tipos de dados: df.dtypes para saber se cada coluna está no formato correto.

    Descrição estatística:

        Numéricos: df.describe()

        Categóricos: df.describe(include='object')

2. Qualidade dos dados

    Valores ausentes: df.isnull().sum() e proporção de valores nulos.

    Duplicados: df.duplicated().sum()

    Erros e inconsistências:

        Formato de datas (ex.: pd.to_datetime)

        Valores fora do esperado (ex.: preço negativo)

        Nomes de produtos e categorias inconsistentes (acentos, maiúsculas/minúsculas)

3. Contextualização temporal

    Converter coluna de data para datetime e criar colunas derivadas:

        Dia (.dt.day)

        Mês (.dt.month)

        Dia da semana (.dt.day_name())

        Hora (.dt.hour)

    Validar se há lacunas no período de 5 dias.

    Identificar horários de pico nas vendas.

4. Análise de métricas básicas

    Vendas totais no período.

    Ticket médio: soma das vendas ÷ número de pedidos.

    Quantidade de produtos vendidos.

    Número de clientes únicos.

5. Distribuições e padrões

    Distribuição de preços, descontos e quantidades.

    Produtos mais vendidos (por quantidade e faturamento).

    Categorias mais populares.

    Comparar dias da semana (tendência de pico ou queda).

6. Relacionamentos e correlações

    Correlação entre variáveis numéricas (df.corr() ou sns.heatmap).

    Analisar se o aumento de descontos impacta o volume vendido.

    Se houver dados geográficos, mapear vendas por região.

7. Visualizações essenciais

    Séries temporais: evolução das vendas por hora/dia.

    Barras: top produtos/categorias.

    Boxplots: variação de preços e ticket médio.

    Mapas de calor: correlação ou padrões horários.

8. Insights iniciais

    Identificar padrões de comportamento do cliente.

    Sazonalidade (mesmo em 5 dias, pode haver ciclos diários).

    Produtos de alto giro vs. baixo giro.

💡 Boas práticas:

    Documentar cada passo (pode ser no Jupyter Notebook).

    Criar funções utilitárias para etapas repetitivas (ex.: detecção de nulos, gráficos padrão).

    Se possível, já separar variáveis para análises futuras de previsão ou segmentação.