with base_producao as (

select distinct * from "FatoOrdemProducao" 
where "dataCriacaoOp" < '2050-01-01'

)
,

base_producao_sistema_novo  as (

select 
	distinct
	a."id",
	a."codigoOp",
	a."maquinaId",
	a."qtdTotalProduzida",
	a."qtdTotalFaltante",
	b."qtdProduzir" as qtd_original,
	a."qtdTotalDefeito",
	a."dataInicioProd",
	a."dataFimProd",
	a.codigo_usuario,
	
case
	when "qtdTotalProduzida" >= max("qtdProduzir") then '1' -- producao finalizada sistema
	else '0' -- producao em andamento
end as producao_flag

	
from 
	"FatoOrdemProduzida" a 
	inner join "FatoOrdemProducao" b on a."codigoOp" = b."codigoOp"
where 
	"dataInicioProd" >= '2025-08-18' -- data de inicio do sistema
	and "id" not in (45,46) -- ids de teste
group by
	1,2,3,4,5,6,7,8,9,10
	
)


select distinct
	a."codigoOp",
	b."codigoOp",
	a."codigoCor",
	a."qtdProduzir",
	a."dataCriacaoOp",
	a."codigo_cliente",
	a."codigo_produto",
	a."qtde",
	a."qtde_b",
	a."pedido",
	a."chave_produto_cor",
	a."dataPrevistaEntrega",
	
case
	when b."codigoOp" is null and a."dataCriacaoOp" < '2025-08-25' then '1' -- producao finalizada sistema antigo
	when b."codigoOp" is null and a."dataCriacaoOp" > '2025-08-24' then '2' -- producao a ser inciada
	when b."codigoOp" is not null and b."producao_flag" = '1' then '3' -- producao finalizada sistema novo
	when b."codigoOp" is not null and b."producao_flag" = '0' then '4' -- producao em andamento sistema novo
	else '5' -- nao mapeado
end as flag_producao

from
	base_producao a
	left join base_producao_sistema_novo b on a."codigoOp" = b."codigoOp"