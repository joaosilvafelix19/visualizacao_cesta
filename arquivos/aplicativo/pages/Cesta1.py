import os
import pandas as pd

# Path and file name
path = os.path.abspath('dados')
file_name = 'dados_jp.xlsx'
excel_file = os.path.join(path, file_name)

# Debugging output
print(f"Path: {path}")
print(f"File Name: {file_name}")
print(f"Full Path to File: {excel_file}")

# Reading the Excel file
try:
    cesta = pd.read_excel(excel_file)
    print("File read successfully")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
