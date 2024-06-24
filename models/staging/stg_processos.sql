with processos as (
    select 
        lpad(cast(cnpj as string), 14, '0') as cnpj,
        area,
        grauProcesso,
        comarca,
        julgamento,
        case 
            when dataDecisao = '' or dataDecisao is null then null 
            else cast(date(dataDecisao) as date) 
        end as dataDecisao,
        case 
            when dataEncerramento = '' or dataEncerramento is null then null 
            else cast(date(dataEncerramento) as date) 
        end as dataEncerramento,
        uf,
        tribunal,
        ultimoEstado,
        orgaoJulgador,
        citacaoTipo,
        unidadeOrigem,
        juiz,
        cast(valorCausa as float64) as valorCausa,
        cast(valorPredicaoCondenacao as float64) as valorPredicaoCondenacao,
        case when dataEncerramento is null then 1 else 0 end as is_active,
        case when dataEncerramento is not null then 'Concluído' else 'Ativo' end as situacao_processo
    from {{ ref('bq_results') }}
)

select * from processos
