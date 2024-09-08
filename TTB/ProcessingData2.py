import pandas as pd
import os
import csv

"""
Projeto: Leitura e Manipulação de Arquivos CSV de Dados Climáticos

Descrição:
Este projeto tem como objetivo a leitura, manipulação e combinação de arquivos CSV contendo dados climáticos. 
A principal solução oferecida por este código é a capacidade de extrair e organizar dados específicos de múltiplos 
arquivos CSV, combinando-os em um único DataFrame, filtrando e salvando os resultados em um novo arquivo CSV.

Função do Problema:
- Ler arquivos CSV de um diretório específico.
- Extrair dados de colunas especificadas pelo usuário.
- Filtrar os dados de acordo com condições específicas (valores maiores que 0).
- Combinar as colunas filtradas em um novo arquivo CSV.
- Permitir que o usuário nomeie as colunas no arquivo de saída.

Autor: Wilson Oliveira, Talita Santos e Jandyr Travassos.
Data: 2024

Mais informações em: https://github.com/wnods/TTB-Data/blob/main/README.md
"""

def ipcsv(file, encoding='utf-8'):
    """
    Reads a CSV file with up to n columns
    <I/P>
    file ------> A file name
    <O/P>
    dicy ------> A dictionary with the data fields as keys.
                  It may have just one key
    """
  
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


print("Directory path:", directory_path)
for root, dirs, files in os.walk(directory_path):
    print(f"Current directory: {root}")
    print(f"Files in current directory: {files}")
    for file in files:
       
        if file.endswith('Backup-DataTTB_24_Final.csv'):
          
            file_path = os.path.join(root, file)
            try:
               
                data_dict = ipcsv(file_path, encoding='latin-1')  
                
                df = pd.DataFrame(data_dict)
               
                data_frames.append(df)
                print(f"File {file} loaded successfully.")
            except Exception as e:
                print(f"Error loading file {file}: {e}")


if data_frames:
    final_df = pd.concat(data_frames, ignore_index=True)
    
    print(final_df.head())

   
    column1 = input("Enter the first column name to merge: ")
    column2 = input("Enter the second column name to merge: ")
    column3 = input("Enter the third column name to merge (filter > 0): ")
    column4 = input("Enter the fourth column name to merge (filter > 0): ")
    column5 = input("Enter the fifth column name to merge (filter > 0): ")
    column6 = input("Enter the sixth column name to merge (filter > 0): ")

    # Ask user for the names of the columns in the output CSV file
    column1_name = input(f"Enter the name for '{column1}' column in the output file: ")
    column2_name = input(f"Enter the name for '{column2}' column in the output file: ")
    column3_name = input(f"Enter the name for '{column3}' column in the output file: ")
    column4_name = input(f"Enter the name for '{column4}' column in the output file: ")
    column5_name = input(f"Enter the name for '{column5}' column in the output file: ")
    column6_name = input(f"Enter the name for '{column6}' column in the output file: ")

    
    if all(col in final_df.columns for col in [column1, column2, column3, column4, column5, column6]):
       
        column3_filtered = final_df[column3].apply(pd.to_numeric, errors='coerce').fillna(0)
        column4_filtered = final_df[column4].apply(pd.to_numeric, errors='coerce').fillna(0)
        column5_filtered = final_df[column5].apply(pd.to_numeric, errors='coerce').fillna(0)
        column6_filtered = final_df[column6].apply(pd.to_numeric, errors='coerce').fillna(0)

        filtered_final_df = final_df.copy()
        filtered_final_df[column3] = column3_filtered
        filtered_final_df[column4] = column4_filtered
        filtered_final_df[column5] = column5_filtered
        filtered_final_df[column6] = column6_filtered

       
        merged_column = (
            filtered_final_df[column1].astype(str) + ', ' +
            filtered_final_df[column2].astype(str) + ', ' +
            filtered_final_df[column3].astype(str) + ', ' +
            filtered_final_df[column4].astype(str) + ', ' +
            filtered_final_df[column5].astype(str) + ', ' +
            filtered_final_df[column6].astype(str)
        )

        
        print(f"\nMerged data from columns '{column1}', '{column2}', '{column3}', '{column4}', '{column5}', and '{column6}':\n{merged_column}")

  
        filtered_merged_column = merged_column[
            (filtered_final_df[column3].astype(float) > 0) &
            (filtered_final_df[column4].astype(float) > 0) &
            (filtered_final_df[column5].astype(float) > 0) &
            (filtered_final_df[column6].astype(float) > 0)
        ]

      
        print(f"\nFiltered data from merged column '{column1}', '{column2}', '{column3}', '{column4}', '{column5}', and '{column6}' (values > 0):\n{filtered_merged_column}")

        output_file = 'filter_file.csv'
        filtered_merged_column.to_csv(output_file, index=False, header=[f"{column1_name}, {column2_name}, {column3_name}, {column4_name}, {column5_name}, {column6_name}"])

        print(f"\nFiltered merged data saved to '{output_file}' successfully.")

        
        print(f"\nYou selected columns: '{column1}' ({column1_name}), '{column2}' ({column2_name}), '{column3}' ({column3_name}), '{column4}' ({column4_name}), '{column5}' ({column5_name}), and '{column6}' ({column6_name})")
    else:
        print(f"One or more of the specified columns do not exist in the DataFrame.")
else:
    print("No CSV files found matching the pattern.")

