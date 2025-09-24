# Projeto EuroLaser (Dados)

Este projeto foi realizado para a empresa Eurolaser situada na cidade de Brusque-SC. O que está apresentado neste repositório não contém informações sigilosas.

## Sobre a Eurolaser

A Eurolaser, localizada em Brusque (SC), atua no segmento de confecção oferecendo soluções ágeis e de alta qualidade em corte a laser para a indústria têxtil.

Hoje a empresa conta com mais de 300 clientes ativos, 6 milhões de etiquetas feitas por ano e um parque fábril de 500 m².

Site: https://www.eurolaser.com.br/#

## Objetivo do Projeto

A Eurolaser tinha como principal necessidade a visão gerencial de produtividade dos seus colaboradores. A empresa conta hoje com aproximadamente 10 máquinas e cerca de 30 colaboradores.

O principal ponto era ter a visão de quantidade de peças, valor produzido e tempo médio por colaborador e máquina.

Diante da necessidade de análise de dados de produtividade entendemos que haviam etapas do processo que precisariam ser criadas antes da entrega final em Power BI. Que seriam:

1. Construção de um banco de dados (datamart) para armazenamento de dados de produtividade
2. Análise Exploratória e Descritiva de Dados em Python
3. Construção de APIs
4. ETL dos dados no sistema ERP gravando dados em banco PostgreSQL hospedado no Railway
5. Agendamento dos jobs ETL via agendador de tarefas no servidor do cliente

Com isso tudo feito, conseguimos chegar a entrega final, que foi um Dashboard interativo em Power BI utilizando linguagem DAX e Power Query. Veja cada passo realizado com detalhe

## Documentação

- [Arquitetura do Sistema](docs/arquitetura.md)
- [Modelagem de Dados - SQL](docs/modelagem.md)
- [ETL](docs/etl.md)
- [Schema - Prisma](sql/modelagem/schema.prisma)
- [Query SQL - Exemplo)](sql/querys/fato_ordem_producao.sql)
- [Modelagem de Dados - Power BI](docs/modelagem_powerbi.md)