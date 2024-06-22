import pandas as pd
import os
import csv

def ipcsv(file, encoding='utf-8'):
    """
    Reads a CSV file with up to n columns
    <I/P>
    file ------> A file name
    <O/P>
    dicy ------> A dictionary with the data fields as keys.
                  It may have just one key
    """
    # Dictionary to store data
    dicy = {}

    # Read file
    with open(file, "r", encoding=encoding) as df:
        reader = csv.reader(df, delimiter=',')

        # Iterate over rows
        for row in reader:
            # Skip empty rows
            if not row:
                continue
            
            # Header line
            if row[0].startswith("##"):
                continue

            # Data field line
            if row[0].startswith("#"):
                field_name = row[1].strip()
                if field_name == 'EOF':
                    break
                dicy[field_name] = []
            else:
                # Append data to the corresponding field
                for i, value in enumerate(row):
                    field_key = f"Column_{i+1}"
                    if field_key not in dicy:
                        dicy[field_key] = []
                    dicy[field_key].append(value)

    return dicy

# Directory for data files
directory_path = '../TTB24'

# List to hold all DataFrames
data_frames = []

# Walk through all files in the directory
print("Directory path:", directory_path)
for root, dirs, files in os.walk(directory_path):
    print(f"Current directory: {root}")
    print(f"Files in current directory: {files}")
    for file in files:
        # Check if file ends with '.csv'
        if file.endswith('Data/Backup-DataTTB_24_Final.csv'):
            # Construct the full file path
            file_path = os.path.join(root, file)
            try:
                # Read the CSV file into a dictionary
                data_dict = ipcsv(file_path, encoding='latin-1')  # Specify encoding here
                # Convert dictionary to DataFrame
                df = pd.DataFrame(data_dict)
                # Add the DataFrame to the list
                data_frames.append(df)
                print(f"File {file} loaded successfully.")
            except Exception as e:
                print(f"Error loading file {file}: {e}")

# Concatenate all DataFrames into a single DataFrame
if data_frames:
    final_df = pd.concat(data_frames, ignore_index=True)
    # Output the head of the final DataFrame
    print(final_df.head())

    # Ask user for the column names to merge
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

    # Check if the columns exist in the DataFrame
    if all(col in final_df.columns for col in [column1, column2, column3, column4, column5, column6]):
        # Filter column3, column4, column5, and column6 to values greater than 0
        column3_filtered = final_df[column3].apply(pd.to_numeric, errors='coerce').fillna(0)
        column4_filtered = final_df[column4].apply(pd.to_numeric, errors='coerce').fillna(0)
        column5_filtered = final_df[column5].apply(pd.to_numeric, errors='coerce').fillna(0)
        column6_filtered = final_df[column6].apply(pd.to_numeric, errors='coerce').fillna(0)

        filtered_final_df = final_df.copy()
        filtered_final_df[column3] = column3_filtered
        filtered_final_df[column4] = column4_filtered
        filtered_final_df[column5] = column5_filtered
        filtered_final_df[column6] = column6_filtered

        # Merge the six columns into a new column
        merged_column = (
            filtered_final_df[column1].astype(str) + ', ' +
            filtered_final_df[column2].astype(str) + ', ' +
            filtered_final_df[column3].astype(str) + ', ' +
            filtered_final_df[column4].astype(str) + ', ' +
            filtered_final_df[column5].astype(str) + ', ' +
            filtered_final_df[column6].astype(str)
        )

        # Output the merged column
        print(f"\nMerged data from columns '{column1}', '{column2}', '{column3}', '{column4}', '{column5}', and '{column6}':\n{merged_column}")

        # Filter merged column to values greater than 0 in column3, column4, column5, and column6
        filtered_merged_column = merged_column[
            (filtered_final_df[column3].astype(float) > 0) &
            (filtered_final_df[column4].astype(float) > 0) &
            (filtered_final_df[column5].astype(float) > 0) &
            (filtered_final_df[column6].astype(float) > 0)
        ]

        # Output filtered data
        print(f"\nFiltered data from merged column '{column1}', '{column2}', '{column3}', '{column4}', '{column5}', and '{column6}' (values > 0):\n{filtered_merged_column}")

        # Save filtered data to CSV
        output_file = 'FilteredData.csv'
        filtered_merged_column.to_csv(output_file, index=False, header=[f"{column1_name}, {column2_name}, {column3_name}, {column4_name}, {column5_name}, {column6_name}"])

        print(f"\nFiltered merged data saved to '{output_file}' successfully.")

        # Show the selected column names
        print(f"\nYou selected columns: '{column1}' ({column1_name}), '{column2}' ({column2_name}), '{column3}' ({column3_name}), '{column4}' ({column4_name}), '{column5}' ({column5_name}), and '{column6}' ({column6_name})")
    else:
        print(f"One or more of the specified columns do not exist in the DataFrame.")
else:
    print("No CSV files found matching the pattern.")

