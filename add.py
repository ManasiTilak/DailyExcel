'''
Add certain text at the end of  each cell in a certain column
'''
import pandas as pd

# Load the Excel file
file_path = 'tweets_collection.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

text_to_add = '#CodingAunty'
column_to_add = 'tweet'

# Check if 'tweet' column exists
if column_to_add in df.columns:
    # Add '#CodingAunty' to the end of each cell in the 'tweet' column
    df[column_to_add] = df[column_to_add].astype(str) + text_to_add
else:
    print(f"The {column_to_add} column does not exist in the file.")

# Save the modified DataFrame back to Excel
df.to_excel('modified_excel_file.xlsx', index=False)
