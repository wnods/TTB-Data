<a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a></br> ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)


# TTB_Data

## Meteorological Data Filtering Project on Tatuoca Island

This project is a simple Python application for filtering meteorological data collected from a weather station. The goal is to process and analyze this data to extract useful information.

## Features

- **Data Reading**: The program reads raw data from a CSV file containing meteorological information such as temperature, humidity, atmospheric pressure, etc.

- **Filtering**: Implements filters to select specific data based on criteria such as temperature range, specific dates, or types of weather events.

- **Adaptive for Simple Analysis**: Performs a basic analysis of the filtered data, calculating averages, maxima, minima, and standard deviations of the meteorological variables.

## Project Folder Structure

- **Data**: Project Data
- **Reader**: Code used to read the CSV Document containing the Backup data.
- **main.py**: Main file that contains the code to read, filter, and analyze meteorological data.
- **data.csv**: Example file containing meteorological data in CSV format for testing purposes.
- **filter.py**: Date filtering of the CSV file already done.

### TTB24

- **Data**
  - `/Document.CSV`
  
- **Reader**
  - `/CSV.py`
  
- **FilterDate.py**: [filter.py]

- **ProcessingData.py**: [main.py]

- **ProcessingData2.py**: [main.py]
    
## How to Use

### Prerequisites

- Python installed.
- Libraries: Pandas

### Installation

1. Clone the repository: `git clone https://github.com/wnods/TTB_Data.git`
2. Navigate to the project directory: `cd repository-name`

## Execution

1. Run the main script: `python3 ProcessingData.py` or `ProcessingData2.py`
2. Follow the instructions on the console to filter the data as needed.

### Usage Example

- **ProcessingData.py**: This script filters data from 3 different columns.
  - The first two columns named in the input choice must be: Column_1 and Column_2, which are respectively Date and Time.
  - The 3rd column (Column_3) is freely chosen.

- **ProcesingData2.py**: This script extends the functionality to filter data from 6 columns.
  - Columns 1 and 2 must still be inserted, and the remaining columns are free to choose.
  - This allows working with more variables: Wind, Gust, Wind Direction, Solar Radiation, Rain.

The program will display the filtering and analysis results directly on the console.

- **FilterDate.py**: This script provides a general reading of the data by line or specific date.
  - Use Column 1 since it is a '.csv' file, and the line is free.
  - The best data from `Data/Backup-DataTTB_24_Final.csv` is only visible from the date and time: 10/05/2024 17:55. Column 1 and Line 147.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.
