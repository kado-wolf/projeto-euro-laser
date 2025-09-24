# ETL - Extract | Transform | Load

Para o projeto realizamos o consumo de 4 principais Apis (Produtos, Pedidos, Ordens de Produção e Clientes). Também criamos um processo para ETL dos dados de usuários, máquinas e marcas que não serão expostos neste repositório.

# ETL de Produtos

Nesse ETL fizemos o consumo de uma lista de produtos do cliente, aplicando algumas transformações e padronizações para salvar no novo datamart criado.

Obs: Os arquivos ipynb foram transformados em .py posteriormente.

## Bibliotecas

![alt text](image.png)

## Consumo da API

![alt text](image-1.png)

## Funções

![alt text](image-2.png)

## Validação

Foram encontrados alguns casos em que temos produtos em Ordens de Produção que não estão em "Produtos" para isso fizemos a validação abaixo e os que encontramos inserimos na tabela com as demais informações como "Não Identificado".

![alt text](image-3.png)

## Load
![alt text](image-4.png)

*Para mais detalhes, veja os arquivos completos em \etl\notebooks*


