# TTB_Data
 ## Projeto de filtragem de Dados Meteorológicos na Ilha de Tatuoca. 

 Este projeto consiste em uma aplicação simples em Python para filtrar dados meteorológicos coletados de uma estação meteorológica. O objetivo é processar e analisar esses dados para extrair informações úteis.

## Funcionalidades:

 Leitura de Dados: O programa lê dados brutos de um arquivo CSV contendo informações meteorológicas como temperatura, umidade, pressão atmosférica, etc.

 Filtragem: Implementa filtros para selecionar dados específicos com base em critérios como faixa de temperatura, datas específicas, ou tipos de eventos meteorológicos.

 Adaptativo para Análise Simples: Realiza uma análise básica dos dados filtrados, calculando médias, máximas, mínimas, e desvios padrão das variáveis meteorológicas.

## Estrutura do Projeto:

main.py: Arquivo principal que contém o código para ler, filtrar e analisar os dados meteorológicos.

data.csv: Arquivo de exemplo contendo os dados meteorológicos em formato CSV para fins de teste.

# Como Usar:
Pré-requisitos:
Python 3 instalado.

# Instalação:
Clone o repositório: git clone https://github.com/wnods/TTB_Data.git
Navegue até o diretório do projeto: cd nome-do-repositorio 

========================

Execução:

Execute o script principal: python3 ProcessingData.py ou ProcessingData2.py

Siga as instruções no console para filtrar os dados conforme necessário.
Exemplo de Uso:

- ProcessingData.py = Trata-se de um código para filtrar 3 dados de diferentes colunas.
  - A ideia é que as duas primeiras colunas nomeadas na escolha do input seja: Column_1 e Column_2 obrigatóriamente, são respectivamente Data e Hora.
  - A 3 coluna, ou melhor, Column_3 é de livre escolha.
- ProcesingData2.py = Segue o mesmo sentido do primeiro código com adendos que é a possibilidade de trabalhar com uma filtragem de 6 colunas.
  - As Column_1 e Column_2 continuam obrigatóriamente a ser inseridas e as restantes são livres.
  - A ideia é que possamos trabalhar com mais variavéis: Vento, Gust, Direção de Vento, Radiação Solar, Chuvas.

O programa exibirá os resultados da filtragem e análise diretamente no console.

Há um terceiro script de código chamado de FilterDate.py
- Tem como objetivo uma leitura geral dos dados por linha/data especifica.
- Use coluna 1 por se tratar de um dado em '.csv' e a linha é livre.
- Os melhores dados de 'Data/Backup-DataTTB_24_Final.csv' só são visiveis a partir do dia e horário: 10/05/2024	17:55. Coluna 1 e Linha 147.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request com melhorias ou novas funcionalidades.
