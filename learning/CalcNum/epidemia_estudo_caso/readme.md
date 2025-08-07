


<h1 align="center">  📊 Modelagem da Dinâmica de Doenças com EDOs – SIR, SIRS e SIRV </h1>



<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=%20Done&color=GREEN&style=for-the-badge"/>
</p>
---



[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![EDO](https://img.shields.io/badge/Math-EDO-green.svg)](LICENSE)

Este projeto apresenta uma simulação computacional do espalhamento de uma doença utilizando **métodos numéricos para resolver sistemas de Equações Diferenciais Ordinárias (EDOs)**. Os modelos abordados são os clássicos **SIR**, **SIRS** e **SIRV**, amplamente utilizados em epidemiologia para prever e analisar a evolução de doenças infecciosas em populações.

## Objetivo

Aplicar o método de **Runge-Kutta de quarta ordem** para resolver numericamente os sistemas de EDOs representando os seguintes modelos:

- **SIR**: Modelo Suscetível–Infectado–Recuperado
- **SIRS**: Modelo com perda de imunidade
- **SIRV**: Modelo com vacinação


## Descrição
Este projeto utiliza modelos matemáticos para simular e analisar a propagação de epidemias. Ele implementa os modelos SIR e SIRS para estudar diferentes cenários, como distanciamento social e perda de imunidade.

## Modelos Implementados
1. **SIR**: Modelo clássico que divide a população em três grupos:
   - Suscetíveis (S)
   - Infectados (I)
   - Recuperados (R)

2. **SIRS**: Extensão do modelo SIR que permite reinfecção devido à perda de imunidade.

## Simulações
- **Simulação 1**: Modelo SIR básico.
- **Simulação 2**: Modelo SIR com distanciamento social.
- **Simulação 3**: Modelo SIRS com perda de imunidade.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias listadas no arquivo `requirements.txt`.
3. Execute os scripts de simulação para gerar os gráficos e análises.

## Interpretação dos Resultados
Os gráficos gerados mostram a evolução das populações ao longo do tempo:
- Suscetíveis (S)
- Infectados (I)
- Recuperados (R)

Cada simulação demonstra o impacto de diferentes parâmetros, como taxa de infecção e perda de imunidade, na dinâmica da epidemia.

## Resultados Esperados

Cada modelo foi simulado com dois conjuntos de parâmetros para comparar o comportamento da doença:

- Evolução das populações Suscetível, Infectado, Recuperado (e Vacinado, no modelo SIRV)

- Gráficos de pico de infecção

- Discussão dos efeitos da imunidade e vacinação

- Avaliação da eficiência de medidas como o distanciamento social

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou novos modelos. Abra um pull request com suas alterações.

---
# Author

| [<img src="https://avatars.githubusercontent.com/u/79289647?v=4" width=115><br><sub>Carlos Hayden</sub>](https://github.com/JunhaumHayden) |
| :---: |