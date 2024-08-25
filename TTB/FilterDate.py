import pandas as pd
import os

"""

Projeto: Extração e Manipulação de Dados Climáticos a partir de Arquivos CSV

Descrição:
Este projeto é destinado à leitura e manipulação de arquivos CSV que contêm dados climáticos. O código permite
a extração de dados específicos de múltiplos arquivos CSV em um diretório, oferecendo a capacidade de selecionar
colunas e linhas para análise detalhada. O principal objetivo é consolidar os dados extraídos em um único DataFrame,
facilitando a análise e o processamento posterior.

Função do Problema:
- Percorrer um diretório para encontrar arquivos CSV específicos.
- Ler os arquivos CSV e carregá-los em DataFrames usando a biblioteca pandas.
- Permitir ao usuário selecionar colunas e linhas específicas para extração de dados.
- Consolidar todos os DataFrames em um único DataFrame para análise unificada.

Autor: Wilson Oliveira, Talita Santos e Jandyr Travassos.
Data: 2024

Mais informações em: https://github.com/wnods/TTB-Data/blob/main/README.md
"""

# Function to read CSV and return DataFrame
def read_csv_to_dataframe(file_path, encoding='latin-1'):
    df = pd.read_csv(file_path, encoding=encoding)
    return df

# Directory of the files
directory_path = '../TTB24'

# List to store all DataFrames
data_frames = []

# Traverse all files in the directory
print("Directory:", directory_path)
for root, dirs, files in os.walk(directory_path):
    print(f"Current directory: {root}")
    print(f"Files in the current directory: {files}")
    for file in files:
        # Check if the file ends with '.csv'
        if file.endswith('Backup-DataTTB_24_Final.csv'):
            # Construct the full file path
            file_path = os.path.join(root, file)
            try:
                # Read the CSV file into a DataFrame using pandas
                df = read_csv_to_dataframe(file_path)

                # Display the first few rows of the DataFrame
                print(f"\nTop columns of the file {file}:")
                print(df.head())

                # Ask the user for the columns to be extracted
                column_index = int(input(f"\nEnter the column index (1-based) to extract data from file {file}: ")) - 1

                # Check if the column index is valid
                if not (0 <= column_index < len(df.columns)):
                    print(f"Invalid column index. Skipping file {file}.")
                    continue

                # Ask the user for the row to be extracted
                row_index = int(input(f"Enter the row index (1-based) to extract data from file {file}: ")) - 1

                # Check if the row index is valid
                if not (0 <= row_index < len(df)):
                    print(f"Invalid row index. Skipping file {file}.")
                    continue

                # Extract the specified column and row
                selected_data = df.iloc[row_index, column_index]
                selected_column = df.iloc[:, column_index]
                selected_row = df.iloc[row_index, :]

                print(f"\nData extracted from file {file}, column {column_index + 1}:\n{selected_column}")
                print(f"\nData extracted from file {file}, row {row_index + 1}:\n{selected_row}")

                # Add the DataFrame to the list
                data_frames.append(df)
                print(f"File {file} loaded successfully.")
            except Exception as e:
                print(f"Error loading or processing file {file}: {e}")

# Concatenate all DataFrames into a single DataFrame
if data_frames:
    final_df = pd.concat(data_frames, ignore_index=True)
    # Display the first few rows of the final DataFrame
    print(final_df.head())
else:
    print("No CSV files found matching the pattern.")

