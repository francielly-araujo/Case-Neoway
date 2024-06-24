import pandas as pd
import os

def clean_csv(file_path, delimiter):
    try:
        # Ler o arquivo CSV com delimitador correto
        df = pd.read_csv(file_path, delimiter=delimiter, encoding='utf-8', engine='python')

        # Remover espaços em branco das colunas
        df.columns = df.columns.str.strip()

        # Substituir pontos nos cabeçalhos
        df.columns = df.columns.str.replace('.', '_', regex=False)

        # Remover linhas completamente vazias
        df.dropna(how='all', inplace=True)

        # Substituir valores vazios por NaN e remover linhas com todos NaN
        df.replace('', pd.NA, inplace=True)
        df.dropna(how='all', inplace=True)

        # Tratar colunas de datas
        for col in df.columns:
            if 'data' in col.lower() or 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')

        # Salvar o CSV limpo
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f'{file_path} limpo e salvo com sucesso.')

    except Exception as e:
        print(f'Erro ao processar o arquivo {file_path}: {e}')

# Caminho dos arquivos CSV e seus respectivos delimitadores
files = {
    'seeds/df_empresas.csv': ';',
    'seeds/empresas_nivel_atividade.csv': ';',
    'seeds/empresas_porte.csv': ';',
    'seeds/empresas_saude_tributaria.csv': ';',
    'seeds/empresas_simples.csv': ';',
    'seeds/bq_results.csv': ','
}

# Limpar e salvar todos os arquivos CSV
for file, delimiter in files.items():
    clean_csv(file, delimiter)
