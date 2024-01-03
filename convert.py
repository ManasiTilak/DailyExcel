import pandas as pd

# Path to your .xlsx file
excel_file_path = 'tweets_aws.xlsx'  # Replace with the path to your .xlsx file

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Convert to CSV
csv_file_path = 'tweets_aws.csv'  # Replace with your desired CSV file name
df.to_csv(csv_file_path, index=False)
