import json
import pandas as pd

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = []
        for line in f:
            data.append(json.loads(line))

    # Flatten the JSON data
    flat_data = []
    for entry in data:
        for parte in entry['partes']:
            flat_entry = {**parte, **{k: entry[k] for k in entry if k != 'partes'}}
            flat_data.append(flat_entry)

    df = pd.DataFrame(flat_data)
    df.to_csv(csv_file, index=False, encoding='utf-8')

json_file = r'C:\Users\franc\neoway_case_analista_bi\raw_data\bq-results-20240515-184938-1715799987947.json'
csv_file = r'C:\Users\franc\neoway_case_analista_bi\seeds\bq_results.csv'
convert_json_to_csv(json_file, csv_file)
