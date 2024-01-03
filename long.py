'''
Identifies if number of characters exceed a certain limit
'''

import pandas as pd

# Load the Excel file
file_path = 'tweets_collection.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)
LIMIT = 270

# Determine if the tweet is "long" (> 270 characters)
df['long'] = df['count'].apply(lambda x: 1 if x > LIMIT else 0)

# Write the DataFrame back to the Excel file
df.to_excel(file_path, index=False)
