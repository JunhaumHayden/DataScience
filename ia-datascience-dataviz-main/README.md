# IA aplicada a Data Science: utilizando IA na construção de visualização de dados

Boas-vindas a mais um curso de **inteligência artificial** da Alura! 

Esse Github foi produzido com muito carinho para você montar o seu portfólio com as atividades do curso e elaborar suas próprias hipóteses, testar as técnicas exploradas dentro do curso e também adicionar outras durante a prática conciliando a linguagem Python e o suporte de ferramentas de IA como o ChatGPT. Tudo isso voltado ao tema de visualização de dados.

O objetivo deste curso é auxiliar você a utilizar o ChatGPT como um assistente pessoal para agilizar as análises de dados e gerar visualizações refinadas por meio da linguagem Python. Você irá aprender a combinar os conhecimentos prévios de análise de dados junto ao auxílio das respostas do ChatGPT por meio de prompts elaborados que visam extrair, tratar e visualizar dados em um projeto prático. Este projeto possibilita sair da leitura de dados de arquivos .CSV extraído deste repositório até a geração de visuais em Python para a construção de um storytelling para um relatório.

É importante que você tenha um **conhecimento básico** das **bibliotecas de visualização** de Python, bem como da **biblioteca de manipulação de dados** do **Pandas**.

## Introdução

<img src="https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/logos/logo_branca_fundo_azul.png" alt="inserir alt">

Neste curso, vamos trabalhar com o storytelling da empresa fictícia **Zoop**, uma grande varejista que atende a todas as regiões do Brasil por meio do seu **e-commerce**. Ela é conhecida pela ampla variedade em seus produtos buscando atender a todo tipo de público.

Para gerenciar o seu alcance, bem como o faturamento de seu setor em lojas online, ela consolida os dados em diferentes períodos de tempo e avalia esses dados para gerar insights e tomar algumas decisões estratégicas em seu negócio. Neste projeto, vamos ter acesso aos dados de parte da sua clientela do e-commerce dentro do ano de 2023.  

Você, como **analista de dados** da empresa, precisará gerar visuais que auxiliem na construção de relatórios de acordo com algumas premissas passadas pelas partes interessadas realizando uma rápida análise do público que possuimos na loja virtual e do faturamento da empresa.

### **Problema de negócio:**

O time de dados da **Zoop** precisa extrair os dados e gerar informações por meio de visuais que possam ser apresentados a diretoria da empresa apontando os dados de faturamento, perfil do cliente e outros indicadores que possam auxiliar na tomada de decisão em sua loja online.

### **Base de dados**

Vamos importar duas bases de dados:

> Dados de clientes do e-commerce da Zoop, separados pelo código identificador da compra.

> Dados de vendas do e-commerce da Zoop em 2023, separados pelo código identificador da compra.

Esses dados serão lidos a partir do repositório compartilhado pelo GitHub.

### **Desafio**

Você, como analista de dados do time de dados da Zoop, tem o desafio de extrair os dados de ambas as bases e construir visuais que possam agregar valor a apresentação dos resultados da Zoop em 2023. Para isso, serão repassados ao todo **7 questionamentos** que foram separados para que você possa contribuir na construção do storytelling das vendas da empresa.

Para agilizar o processo da análise exploratória dos dados (AED) e a criação dos visuais, utilizaremos a IA do **ChatGPT** como nossa assistente, tudo isso levando em conta o prazo curto para as análises e a qualidade da entrega.

## Paleta de Cores

Neste projeto, utilizaremos a paleta de cores abaixo, passada por meio de uma entrevista com o time de UX/UI da Zoop.

Vamos explorar a importância das cores na visualização de dados, discutir como as pessoas percebem e interpretam as informações visuais, e abordar a diferença entre a capacidade da inteligência artificial e a visão humana no que diz respeito à escolha de cores e acessibilidade.

|Vermelho|||
|------|------|------|
| VERMELHO_1 |VERMELHO_2 |VERMELHO_3 |
|#e23155 | #cc2c4e| #b32742 |
| ![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/VERMELHO_1.png)  |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/VERMELHO_2.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/VERMELHO_3.png) |

&nbsp;

|Azul|||
|------|------|------|
| AZUL_1 |AZUL_2 |AZUL_3 |
|#203f75 | #1c3867| #19325b |
| ![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AZUL_1.png)  |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AZUL_2.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AZUL_3.png) |

&nbsp;

|Cinza||||||
|------|------|------|------|------|------|
|BRANCO| CINZA_1 |CINZA_2 |CINZA_3 |CINZA_4 |CINZA_5 |
|#ffffff | #ebebeb | #d9d9d9| #cccccc | #555655| #231f20 |
| ![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/BRANCO.png)  |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/CINZA_1.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/CINZA_2.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/CINZA_3.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/CINZA_4.png)|![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/CINZA_5.png)|

&nbsp;

|Aqua|||
|------|------|------|
| AQUA_1 |AQUA_2 |AQUA_3 |
|#addcd4 | #9fccc5| #96bfb9 |
| ![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AQUA_1.png)  |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AQUA_2.png) |![adicionar desc](https://raw.githubusercontent.com/alura-cursos/ia-datascience-dataviz/main/imagens/paleta_cores/AQUA_3.png) |

&nbsp;

Como sugestão para outros projetos que você desenvolver, existem sites como o [Coolor](https://coolors.co/palettes/trending) ou [imagecolorpicker](https://imagecolorpicker.com/) que fornecem ideias de paletas e cores que ornam bem se relacionadas.

## Visualizações que exploraremos

Na imagem abaixo, apresentamos um diagrama com diversos tipos de **visualização de dados** (criado por [Andrew Abela](https://extremepresentation.com/wp-content/uploads/choosing-a-good-chart-09-1.pdf)) em que é possível perceber **4 subgrupos**, dentre eles:

- Comparação
- Distribuição
- Relacionamento
- Composição

![Diagrama de Visualização de Dados (Andrew Abela - Traduzido por Afonso Rios)](https://github.com/alura-cursos/ia-datascience-dataviz/blob/main/imagens/Tipos_Graficos/Diagrama%20de%20Visualiza%C3%A7%C3%A3o%20de%20Dados%20(Andrew%20Abela%20-%20Traduzido%20por%20Afonso%20Rios).png)

Para este curso, focamos nos seguintes visuais:

- Gráfico de Colunas
- Gráfico de Barras
- Gráfico de Linha
- Gráficos de Barras e Colunas Empilhadas
- Gráficos de Setores (Pizza e Rosca)
- Histograma
- Boxplot

## Gráficos Produzidos

Para acessar as imagens dos principais gráficos gerados ao longo curso clique nesse [link](https://github.com/alura-cursos/ia-datascience-dataviz/tree/main/imagens/Tipos_Graficos/graficos).

## Conclusões

Esse curso teve como objetivo utilizar o ChatGPT como assistente pessoal na análise e geração de visualização de dados aliado a Linguagem Python visando o desenvolvimento de um storytelling sobre as vendas e perfil dos clientes de uma empresa fictícia.

Exploramos os processos de extração, tratamento e visualização de dados, criação de scripts em Python personalizados de acordo com os prompts executados no ChatGPT e reconhecimento das limitações e possibilidades do uso de IAs na otimização de processos de análise e visualização de dados.

Além disso, criamos gráficos dos mais diversos tipos partindo do uso das bibliotecas mais utilizadas em Python, personalizando-os e adicionando recursos visuais como anotações, destaques, legenda de dados e outras técnicas de visualização. 

Ao concluir este curso, você será capaz de gerar um **Jupyter Notebook** (Google Colab) com o processo da análise exploratória dos dados, visualizações personalizadas e voltadas ao tipo de público que você deseja, combinando a linguagem Python com o ChatGPT.

Sinta-se à vontade para fazer o fork desse projeto e construir o seu portfólio 😊

