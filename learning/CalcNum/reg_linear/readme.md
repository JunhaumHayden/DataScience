

Neste curso, iremos estabelecer o preço de venda de casas, analisando as diversas características que influenciam sua precificação. Para alcançar esse objetivo, vamos utilizar a regressão linear como metodologia. Vale lembrar que todas as análises serão realizadas no Colab para facilitar o processo.

Por isso, é importante que você faça o download do notebook com a estrutura do projeto que será construído ao longo dessa jornada de aprendizado.
Base de dados

Utilizamos como inspiração a famosa base de dados House Price do Kaggle. Fizemos algumas transformações na base original para garantir um melhor aprendizado das técnicas apresentadas neste curso. Faça o download da base de dados e, em seguida, carregue o arquivo no Colab.

Confira abaixo os campos disponíveis para análise:

    area_primeiro_andar: Refere-se à área do primeiro andar da propriedade, medida em metros quadrados.
    existe_segundo_andar: Esta variável é binária, indicando se a propriedade possui ou não um segundo andar. Pode ser representada como 1 para "sim" e 0 para "não".
    area_segundo_andar: Se a propriedade tiver um segundo andar, esta variável representa a área total do segundo andar, medida em metros quadrados.
    quantidade_banheiros: Indica o número total de banheiros na propriedade.
    capacidade_carros_garagem: Esta variável indica a capacidade da garagem da propriedade, ou seja, o número máximo de carros que podem ser estacionados na garagem.
    qualidade_da_cozinha_Excelente: Esta é uma variável categórica que avalia a qualidade da cozinha na propriedade. Neste caso, assume-se que se a cozinha for considerada "Excelente" é representada por 1, e caso contrário, por 0.
    preco_de_venda: Este é o preço de venda da propriedade em reais. É a variável alvo que se tenta prever usando os outros atributos da propriedade.

