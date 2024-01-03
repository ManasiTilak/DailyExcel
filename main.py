import pandas as pd

# Load the Excel file
file_path = 'tweets_collection.xlsx' 
df = pd.read_excel(file_path)

# Count the number of characters in each tweet
df['count'] = df['tweet'].apply(len)

# Write the DataFrame back to the Excel file
df.to_excel(file_path, index=False)
