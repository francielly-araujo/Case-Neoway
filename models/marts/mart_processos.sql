with processos as (
    select 
        lpad(cast(cnpj as string), 14, '0') as cnpj,
        situacao_processo,
        is_active
    from {{ ref('stg_processos') }}
)

, resumo as (
    select 
        cnpj,
        count(*) as total_processos,
        sum(is_active) as processos_ativos,
        sum(case when is_active = 0 then 1 else 0 end) as processos_concluidos,
        round(sum(case when is_active = 0 then 1 else 0 end) / count(*) * 100, 2) as percentual_concluidos
    from processos
    group by cnpj
)

select * from resumo
