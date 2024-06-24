# Case Neoway

Este repositório contém o projeto desenvolvido para o Case Neoway, incluindo scripts para tratamento de dados, modelos do dbt, e o arquivo do dashboard em Power BI.

## Estrutura do Repositório

- `dbt/`: Contém os modelos do dbt utilizados para transformar e organizar os dados.
- `scripts/`: Scripts em Python para tratamento inicial dos dados.
- `Case_Neoway.pbix`: Arquivo do Power BI com o dashboard desenvolvido.

## Instruções para Reproduzir o Projeto

### Requisitos

- Python 3.x
- dbt 1.8.1
- Power BI Desktop

### Passos

1. Clone o repositório:
    ```sh
    git clone https://github.com/francielly-araujo/Case-Neoway.git
    cd Case-Neoway
    ```

2. Configure e execute os scripts em Python para tratamento dos dados:
    ```sh
    python scripts/corrigir_csv.py
    ```

3. Configure e execute os modelos do dbt:
    ```sh
    dbt seed
    dbt run
    ```

4. Abra o arquivo `Case_Neoway.pbix` no Power BI Desktop para visualizar o dashboard.

## Contato

Para mais informações, entre em contato com francielly.souza.araujo@gmail.com
