with uf_estado as (
    select 'AC' as uf, 'Acre' as estado union all
    select 'AL', 'Alagoas' union all
    select 'AP', 'Amapa' union all
    select 'AM', 'Amazonas' union all
    select 'BA', 'Bahia' union all
    select 'CE', 'Ceara' union all
    select 'DF', 'Distrito Federal' union all
    select 'ES', 'Espirito Santo' union all
    select 'GO', 'Goias' union all
    select 'MA', 'Maranhao' union all
    select 'MT', 'Mato Grosso' union all
    select 'MS', 'Mato Grosso do Sul' union all
    select 'MG', 'Minas Gerais' union all
    select 'PA', 'Para' union all
    select 'PB', 'Paraiba' union all
    select 'PR', 'Parana' union all
    select 'PE', 'Pernambuco' union all
    select 'PI', 'Piaui' union all
    select 'RJ', 'Rio de Janeiro' union all
    select 'RN', 'Rio Grande do Norte' union all
    select 'RS', 'Rio Grande do Sul' union all
    select 'RO', 'Rondonia' union all
    select 'RR', 'Roraima' union all
    select 'SC', 'Santa Catarina' union all
    select 'SP', 'Sao Paulo' union all
    select 'SE', 'Sergipe' union all
    select 'TO', 'Tocantins'
)

, empresas as (
    select
        cast(cnpj as string) as cnpj,
        cast(dt_abertura as string) as dt_abertura,
        cast(matriz_empresaMatriz as string) as matriz_empresaMatriz,
        lpad(cast(cd_cnae_principal as string), 14, '0') as cd_cnae_principal,
        de_cnae_principal,
        de_ramo_atividade,
        de_setor,
        lpad(cast(endereco_cep as string), 8, '0') as endereco_cep,
        endereco_municipio,
        e.endereco_uf,
        'Brasil' as pais,
        endereco_regiao,
        endereco_mesorregiao,
        situacao_cadastral,
        u.estado as nome_estado
    from `neoway-426801`.`Empresas`.`df_empresas` e
    join uf_estado u
    on e.endereco_uf = u.uf
)

select * from empresas
