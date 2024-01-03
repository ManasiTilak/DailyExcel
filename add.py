import pandas as pd

# Load the Excel file
file_path = 'tweets_collection.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Check if 'tweet' column exists
if 'tweet' in df.columns:
    # Add '#CodingAunty' to the end of each cell in the 'tweet' column
    df['tweet'] = df['tweet'].astype(str) + ' #CodingAunty'
else:
    print("The 'tweet' column does not exist in the file.")

# Save the modified DataFrame back to Excel
df.to_excel('modified_excel_file.xlsx', index=False)
