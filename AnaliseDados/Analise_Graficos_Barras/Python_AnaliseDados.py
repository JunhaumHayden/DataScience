import pandas as pd
#If you are importing a package that is not installed, you can install it by running the following command in an activated terminal: python -m pip install {package_name}
import plotly.express as px

#pd.read -> Alias do Pandas usa o metodo read para ler o arquivo com o caminho e as abas(sheet_name) no argumento do metodo
df_principal = pd.read_excel('./IPy-TabeActions.xlsx', sheet_name = 'Principal')
df_principal
#Usar [[]] para passar as colunas
df_principal = df_principal[['Ativo','Data','Último (R$)','Var. Dia (%)']].copy()
df_principal
#Para renomear as colunas com caracteres especiais
df_principal = df_principal.rename(columns={'Último (R$)':'valor_final','Var. Dia (%)':'valor_dia_100' }).copy()
df_principal
#criar uma nova coluna 'vlr_pct' no dataframe que ira receber o valor da coluna 'valor_dia_100'/100
df_principal['vlr_pct'] = df_principal['valor_dia_100']/100
df_principal

df_principal['valor_inicial'] = df_principal['valor_final']/(df_principal['vlr_pct']+1)
df_principal
#pd.read -> Criar um dataframe. Alias do Pandas usa o metodo read para ler o arquivo com o caminho e as abas(sheet_name) no argumento do metodo
df_total_de_acoes = pd.read_excel('./IPy-TabeActions.xlsx', sheet_name = 'Total_de_acoes')
df_total_de_acoes
#.merge para juntar as colunas da dataframe total_acoes no dataframe principal
#left_on serve como chave para a junçao (o que tem na coluna 'Ativo) right_on compara os valores na coluna 'Código'
df_principal = df_principal.merge(df_total_de_acoes, left_on='Ativo', right_on='Código',how='left')
df_principal

df_principal.info()
# Verifica se a coluna 'Código' existe antes de executar o drop
if 'Código' in df_principal.columns:
    df_principal = df_principal.drop(columns=['Código'])
    
df_principal

df_principal['variacao_rs'] = (df_principal['valor_final'] - df_principal['valor_inicial'])* df_principal['Qtde. Teórica']
df_principal

#para formatar as casas decimais no pandas
pd.options.display.float_format = '{:.2f}'.format
df_principal

#atibuindo o tipo de variavel (int) para a quantidade
df_principal['Qtde. Teórica'] = df_principal['Qtde. Teórica'].astype(int)
df_principal

#Para renomear as colunas com caracteres especiais
df_principal = df_principal.rename(columns={'Qtde. Teórica':'QtdeTeorica'}).copy()
df_principal

# Criando a coluna 'Status' usando uma expressão lambda
df_principal['resultado'] = df_principal['variacao_rs'].apply(lambda x: 'SUBIU' if x > 0 else ('DESCEU' if x < 0 else 'ESTAVEL'))
df_principal

#pd.read -> Criar um dataframe. Alias do Pandas usa o metodo read para ler o arquivo com o caminho e as abas(sheet_name) no argumento do metodo
df_Ticker = pd.read_excel('./IPy-TabeActions.xlsx', sheet_name = 'Ticker')
df_Ticker

#.merge para juntar as colunas da dataframe total_acoes no dataframe principal
#left_on serve como chave para a junçao (o que tem na coluna 'Ativo) right_on compara os valores na coluna 'Código'
df_principal = df_principal.merge(df_Ticker, left_on='Ativo', right_on='Ticker',how='left')
df_principal

df_principal.info()
# Verifica se a coluna 'Código' existe antes de executar o drop
if 'Código' in df_principal.columns:
    df_principal = df_principal.drop(columns=['Ticker'])
    
df_principal

# Criando a coluna 'Status' usando uma expressão lambda
df_principal['Status'] = df_principal['idade'].apply(lambda x: 'MAIS QUE 100' if x > 100 else ('Menor que 50' if x < 50 else 'De 50 a 100'))
df_principal

#calculando o maior valor
maior = df_principal['variacao_rs'].max()

#calculando o menor valor
menor = df_principal['variacao_rs'].min()

#calculando o mediar do valor
media = df_principal['variacao_rs'].mean()

#calculando o mediar do quem subiu
media_subiu = df_principal[df_principal['resultado'] == 'SUBIU']['variacao_rs'].mean()

#calculando o mediar do quem desceu
media_desceu = df_principal[df_principal['resultado'] == 'DESCEU']['variacao_rs'].mean()

#imprimindo
print(f'Maior/R$ {maior:,.2f}')
print(f'Menor/R$ {menor:,.2f}')
print(f'Media/R$ {media:,.2f}')
print(f'Media de quem subiu/R$ {media_subiu:,.2f}')
print(f'Media de quem desceu/R$ {media_desceu:,.2f}')

#calculando o mediar do quem subiu e armazenando em um dataframe
df_principal_subiu = df_principal[df_principal['resultado'] == 'SUBIU']
df_principal_subiu

#somando acoes que subiram separando por seguimento e armazenando em um dataframe
#.reset_index serve para que não seja criado uma lista e os dados permanecam em um dataframe
df_analise_segmento = df_principal_subiu.groupby('seguimento')['variacao_rs'].sum().reset_index()
df_analise_segmento

#somando acoes que subiram separando por seguimento e armazenando em um dataframe
#.reset_index serve para que não seja criado uma lista e os dados permanecam em um dataframe
df_analise_saldo = df_principal.groupby('resultado')['variacao_rs'].sum().reset_index()
df_analise_saldo

#Necessario importar a biblioteca plotly.express
#.bar refere-se a um grafico de barras, x e y são os eixos do grafico, text texto no grafico, title titulo do grafico
#.show para apresentar o grafico
fig = px.bar(df_analise_saldo,x='resultado', y='variacao_rs', text='variacao_rs', title='variacao resultados em Reais')
fig.show()

#Necessario importar a biblioteca plotly.express
#.bar refere-se a um grafico de barras, x e y são os eixos do grafico, text texto no grafico, title titulo do grafico
#.show para apresentar o grafico
fig_seg = px.bar(df_analise_segmento,x='seguimento', y='variacao_rs', text='variacao_rs', title='variacao resultados por SEGUIMENTO')
fig_seg.show()

df_analise_cat_idade = df_principal.groupby('idade')['variacao_rs'].sum().reset_index()
df_analise_cat_idade

fig_idade = px.bar(df_analise_cat_idade, x='idade', y='variacao_rs', text='variacao_rs', title='Variação Reais por Categoria de IDADE')
fig_idade.show()
