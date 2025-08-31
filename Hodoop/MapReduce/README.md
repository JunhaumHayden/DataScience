# PythonCodes
Codes in Python



<h1 align="center"> Program developed in Python to illustrate how MapReduce works </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Description

English

Project in development for the discipline of Big Data Topics in Python at Faculdade Estácio de Sá.
It is about concepts and applications of the principles of Big Data, Internet of Things, distributed computing, cloud platforms, processing and data flow.
The Project seeks to exemplify the architecture of Hadoop, its ecosystem and its solutions; comparison between Hadoop distributed file system (HDFS) and relational database management system (RDBMS); data lake concepts.

Hadoop is an open source framework technology developed by the Apache Foundation, being applied to the storage and processing of large volumes of data, that is, Big Data. In addition to the Apache free distribution, Hadoop has other distributions, such as:
Cloudera;
Hortonworks;
MapR;
IBM;
Microsoft Azure;
Amazon Web Services Elastic MapReduce Hadoop Distribution.

###Example of MapReduce

To reproduce the examples presented, the Windows 10 operating system and the installed PyCharm and Java 8 programs were used. In addition to Hadoop.
The MapReduce engine is a fundamental component in the Hadoop architecture to apply distributed computing and thus improve program performance.

The example program developed in Python to illustrate how MapReduce works. For that, we will need to follow these steps:

 1- Install Python and configure the environment;
 2- Develop the MapReduce program;
 3- Run the program and analyze the results.


After installing PyCharm, install the mrjob package. To do this, just open a Python terminal and run this command line:

 **pip install mrjob**

 mrjob is a Python library that provides features for writing MapReduce code. There is the facility of being able to implement code for the mapping and reduction phases in a single class.

Develop the MapReduce program
After installing mrjob, develop the program. The objective is to receive a text with several words and count how many times each one appeared. Presented in the **principal.py** file.

At the beginning of the program, we import the mrjob library and the re package. The mrjob, as we have seen, is useful for developing the MapReduce application. The re package is used to handle regular expressions, which are very useful computational models for pattern representation and word processing.

Let's understand in more detail what the code does:

The following line of code takes a line of text as input and returns a list of words without the spaces.

**palavra_regex = re.compile(r'[\w]+')**

In the next line of the program, we have:

**class QuantidadePalavras(MRJob):**

This is a declaration for a class in Python. In this case, we named the class “QuantityWords”; in addition, it inherits characteristics from the “MRJob” class of the library that we had already installed. Now we have the mapper and reducer methods, which are respectively responsible for the mapping and reduction phases.

In the mapper method, we process each line and generate pairs of words – which are the keys – and the value 1; in the reducer, the key and value pairs, obtaining the number of times the word appeared in the input data file;

Finally, we have the following block, which is responsible for starting the lifecycle of our process:

  **if __name__ == '__main__':**
    **QuantidadePalavras.run()**

Run the program and analyze the results
To run our example, we will use the file “example_text.txt” with the following content:

This text has repeated words
mapreduce hadoop words
words word hadoop text python
mrjob hadoop mapreduce hadoop mapreduce
To run the program, we must write and execute the command line below in the terminal:

  **python principal.py texto_exemplo.txt > qtd.txt**

We need that, in the case of our example, the file “texto_exemplo.txt” is stored in the same location as the “principal.py” file. When we run the command line, we will get the output file “qtd.txt” with the following content:

**'este'  1**	
 **'hadoop'  4**
 **'mapreduce' 3**
 **'mrjob' 1**
 **'palavra' 1**
 **'palavras'  3**
 **'python'  1**
 **'repetidas' 1**
 **'tem' 1**
 **'texto' 2**


Which is exactly what we wanted to get: the number of times each word appeared in the input text.


Português-Br

Projeto em desenvolvimento para a disciplina de Tópicos de Big Data em Python da Faculdade Estácio de Sá.
Trata-se de conceitos e aplicações dos princípios de Big Data, Internet das Coisas, computação distribuída, plataformas em nuvem, processamento e fluxo de dados.
No Projeto procura-se exemplificar a arquitetura do Hadoop, seu ecossistema e suas soluções; comparação entre sistema de arquivos distribuídos do Hadoop (HDFS) e sistema de gerência de banco de dados relacionais (RDBMS); conceitos de data lake.

O Hadoop é uma tecnologia de framework de software livre desenvolvida pela Apache Foundation, sendo aplicado no armazenamento e no processamento de dados de grandes volumes, ou seja, em Big Data. Além da distribuição livre da Apache, o Hadoop possui outras distribuições, como:

Cloudera;
Hortonworks;
MapR;
IBM;
Microsoft Azure;
Amazon Web Services Elastic MapReduce Hadoop Distribution.

As grandes empresas da internet, como Facebook, Yahoo, Google, Twitter e LinkedIn, entre outras, usam o Hadoop pela natureza de suas aplicações, ou seja, pelos diferentes tipos de dados. Esses dados podem ser:

- Estruturados, como tabelas e planilhas;
- Não estruturados, como logs, corpo de e-mails e texto de blogs;
- Semiestruturados, como metadados de arquivos de mídia, XML e HTML.

A arquitetura do Hadoop é formada por quatros componentes principais:

 ## MapReduce (modelo de programação paralela)

 ## HDFS (sistema de arquivos distribuídos do Hadoop)

 ## YARN (Yet Another Resource Negociator)

 ## Utilitários comuns do Hadoop (Hadoop Common)


###Exemplo de MapReduce

Para reproduzir os exemplos apresentados, foram utilizados o sistema operacional Windows 10 e dos programas PyCharm e Java 8 instalados. Além do Hadoop.
O mecanismo de MapReduce é um componente fundamental na arquitetura do Hadoop para aplicar a computação distribuída e, assim, melhorar o desempenho dos programas.

O exemplo de programa desenvolvido em Python para ilustrar o funcionamento do MapReduce. Para isso, vamos precisar seguir estes passos:

 1- Instalar o Python e configurar o ambiente;
 2- Desenvolver o programa MapReduce;
 3- Executar o programa e analisar os resultados.


Depois de instalar o PyCharm, instalar o pacote mrjob. Para isso, basta abrir um terminal do Python e executar esta linha de comando:

   **pip install mrjob**

O mrjob é uma biblioteca do Python que oferece recursos para escrever códigos MapReduce. Existe a facilidade de poder implementar código para as fases de mapeamento e de redução em uma única classe.

Desenvolver o programa MapReduce
Depois de instalar o mrjob, desenvolver o programa. O objetivo é receber um texto com diversas palavras e contar quantas vezes cada uma apareceu. Apresentado no arquivo **principal.py**.

No início do programa, fazemos a importação da biblioteca mrjob e do pacote re. O mrjob, como vimos, é útil para desenvolver a aplicação MapReduce. Já o pacote re é usado para tratar expressões regulares, que são modelos computacionais muito úteis para representação de padrões e processamento de palavras.

Vamos entender com mais detalhes o que o código faz:

A linha de código a seguir recebe uma linha de texto como entrada e retorna uma lista de palavras sem os espaços.

   **palavra_regex = re.compile(r'[\w]+')**

Na próxima linha do programa, temos:

  **class QuantidadePalavras(MRJob):**

Trata-se de uma declaração para uma classe no Python. No caso, demos o nome da classe de “QuantidadePalavras”; além disso, ela herda características da classe “MRJob” da biblioteca que já havíamos instalado.Agora temos os métodos mapper e reducer, que são respectivamente responsáveis pela fase de mapeamento e redução.

No método mapper, processamos cada linha e geramos pares de palavras – que são as chaves – e do valor 1; no reducer, os pares do tipo chave e valor, obtendo a quantidade de vezes que a palavra apareceu no arquivo de entrada de dados;

Por fim, temos o seguinte bloco, que é responsável por iniciar o ciclo de vida do nosso processo:

  **if __name__ == '__main__':**
    **QuantidadePalavras.run()**

Executar o programa e analisar os resultados
Para executar o nosso exemplo, vamos usar o arquivo “texto_exemplo.txt” com o seguinte conteúdo:

Este texto tem palavras repetidas
mapreduce hadoop palavras
palavras palavra hadoop texto python
mrjob hadoop mapreduce hadoop mapreduce
Para executar o programa, devemos escrever e executar a linha de comando abaixo no terminal:

  **python principal.py texto_exemplo.txt > qtd.txt**

Precisamos que, no caso do nosso exemplo, o arquivo “texto_exemplo” esteja armazenado no mesmo local do arquivo “principal.py”. Quando executarmos a linha de comando, obteremos o arquivo de saída “qtd.txt” com o seguinte conteúdo:

 **'este'  1**	
 **'hadoop'  4**
 **'mapreduce' 3**
 **'mrjob' 1**
 **'palavra' 1**
 **'palavras'  3**
 **'python'  1**
 **'repetidas' 1**
 **'tem' 1**
 **'texto' 2**

Que é exatamente o que queríamos obter: a quantidade de vezes que cada palavra apareceu no texto de entrada.



# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |
