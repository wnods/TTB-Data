import pandas as pd
import os
import csv
import matplotlib.pyplot as plt

def ipcsv(file, encoding='utf-8'):
    dicy = {}
    with open(file, "r", encoding=encoding) as df:
        reader = csv.reader(df, delimiter=',')
        for row in reader:
            if not row:
                continue
            if row[0].startswith("##"):
                continue
            if row[0].startswith("#"):
                field_name = row[1].strip()
                if field_name == 'EOF':
                    break
                dicy[field_name] = []
            else:
                for i, value in enumerate(row):
                    field_key = f"Column_{i+1}"
                    if field_key not in dicy:
                        dicy[field_key] = []
                    dicy[field_key].append(value)
    return dicy

directory_path = '../TTB24'
data_frames = []

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('Backup-DataTTB_24_Final.csv'):
            file_path = os.path.join(root, file)
            try:
                data_dict = ipcsv(file_path, encoding='latin-1')
                df = pd.DataFrame(data_dict)
                data_frames.append(df)
            except Exception as e:
                print(f"Error loading file {file}: {e}")

if data_frames:
    final_df = pd.concat(data_frames, ignore_index=True)
    print(final_df.head())

    # Listar as colunas com índices numéricos
    print("Colunas disponíveis:")
    for i, col in enumerate(final_df.columns):
        print(f"{i + 1}: {col}")
    
    # Selecionar colunas pelo número
    col_indices = []
    for i in range(3):
        while True:
            try:
                index = int(input(f"Escolha o número da coluna {i+1}: ")) - 1
                if 0 <= index < len(final_df.columns):
                    col_indices.append(index)
                    break
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    column1, column2, column3 = final_df.columns[col_indices[0]], final_df.columns[col_indices[1]], final_df.columns[col_indices[2]]
    
    # Solicitar nomes das colunas para o arquivo de saída
    column1_name = input(f"Insira o nome para a coluna '{column1}' no arquivo de saída: ")
    column2_name = input(f"Insira o nome para a coluna '{column2}' no arquivo de saída: ")
    column3_name = input(f"Insira o nome para a coluna '{column3}' no arquivo de saída: ")

    column3_filtered = final_df[column3].apply(pd.to_numeric, errors='coerce').fillna(0)
    filtered_final_df = final_df.copy()
    filtered_final_df[column3] = column3_filtered

    merged_column = filtered_final_df[column1].astype(str) + ', ' + filtered_final_df[column2].astype(str) + ', ' + filtered_final_df[column3].astype(str)
    print(f"\nDados mesclados das colunas '{column1}', '{column2}', e '{column3}':\n{merged_column}")

    filtered_merged_column = merged_column[filtered_final_df[column3].astype(float) > 0]
    print(f"\nDados filtrados da coluna mesclada '{column1}', '{column2}', e '{column3}' (valores > 0):\n{filtered_merged_column}")
    
    output_file = 'DailyRain.csv'
    filtered_merged_column.to_csv(output_file, index=False, header=[f"{column1_name}, {column2_name}, {column3_name}"])
    print(f"\nDados mesclados filtrados salvos em '{output_file}' com sucesso.")

    plt.figure(figsize=(10, 5))
    plt.plot(filtered_final_df[column3].astype(float), label='Precipitação')
    plt.title('Gráfico de Precipitação da Chuva')
    plt.xlabel('Índice')
    plt.ylabel(column3_name)
    plt.legend()
    plt.grid(True)
    plt.savefig('RainPlot.png') 
    plt.show() 
else:
    print("Nenhum arquivo CSV encontrado correspondendo ao padrão.")
