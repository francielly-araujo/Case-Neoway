with processos as (
    select 
        lpad(cast(p.cnpj as string), 14, '0') as cnpj,
        e.de_setor,
        p.situacao_processo,
        p.is_active
    from {{ ref('stg_processos') }} p
    join {{ ref('stg_empresas') }} e
    on lpad(cast(p.cnpj as string), 14, '0') = lpad(cast(e.cnpj as string), 14, '0')
)

, resumo as (
    select 
        de_setor,
        count(*) as total_processos,
        sum(is_active) as processos_ativos,
        sum(case when is_active = 0 then 1 else 0 end) as processos_concluidos,
        round(sum(case when is_active = 0 then 1 else 0 end) / count(*) * 100, 2) as percentual_concluidos
    from processos
    group by de_setor
)

select * from resumo
