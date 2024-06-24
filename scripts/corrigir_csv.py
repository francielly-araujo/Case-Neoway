import pandas as pd

# Carregar os arquivos CSV
df_empresas = pd.read_csv('seeds/df_empresas.csv', dtype={'cnpj': str})
empresas_nivel_atividade = pd.read_csv('seeds/empresas_nivel_atividade.csv', dtype={'cnpj': str})
empresas_porte = pd.read_csv('seeds/empresas_porte.csv', dtype={'cnpj': str})
empresas_saude_tributaria = pd.read_csv('seeds/empresas_saude_tributaria.csv', dtype={'cnpj': str})
empresas_simples = pd.read_csv('seeds/empresas_simples.csv', dtype={'cnpj': str})
bq_results = pd.read_csv('seeds/bq_results.csv', dtype={'cnpj': str})

# Salvar os arquivos CSV com os CNPJs como texto
df_empresas.to_csv('seeds/df_empresas.csv', index=False, quoting=1) # quoting=1 garante que os textos sejam cercados por aspas
empresas_nivel_atividade.to_csv('seeds/empresas_nivel_atividade.csv', index=False, quoting=1)
empresas_porte.to_csv('seeds/empresas_porte.csv', index=False, quoting=1)
empresas_saude_tributaria.to_csv('seeds/empresas_saude_tributaria.csv', index=False, quoting=1)
empresas_simples.to_csv('seeds/empresas_simples.csv', index=False, quoting=1)
bq_results.to_csv('seeds/bq_results.csv', index=False, quoting=1)
