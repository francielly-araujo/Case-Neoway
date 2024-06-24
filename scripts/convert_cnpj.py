import pandas as pd

# Função para formatar CNPJ e CNAE
def format_cnpj(cnpj):
    cnpj_str = str(cnpj)
    return cnpj_str.zfill(14)

def format_cnae(cnae):
    cnae_str = str(cnae)
    return cnae_str.zfill(7)

# Lista de arquivos CSV a serem atualizados
csv_files = [
    'seeds/df_empresas.csv',
    'seeds/empresas_nivel_atividade.csv',
    'seeds/empresas_porte.csv',
    'seeds/empresas_saude_tributaria.csv',
    'seeds/empresas_simples.csv',
    'seeds/bq_results.csv'
]

for file in csv_files:
    # Carregar o CSV
    df = pd.read_csv(file)

    # Formatar as colunas de CNPJ e CNAE, se existirem
    if 'cnpj' in df.columns:
        df['cnpj'] = df['cnpj'].apply(format_cnpj)
    if 'cd_cnae_principal' in df.columns:
        df['cd_cnae_principal'] = df['cd_cnae_principal'].apply(format_cnae)

    # Salvar o CSV corrigido
    df.to_csv(file, index=False)
    print(f"Arquivo {file} atualizado com sucesso.")
