import pandas as pd
import json
from itertools import permutations

# Filepath to your CSV file
csv_file = "/Users/suare111803/Documents/PokeSudoku/pokemondata.csv"

# Load the CSV file
df = pd.read_csv(csv_file)

#Drop rows where 'Type 1' or 'Type 2' is NaN
df = df.dropna(subset=['Type 1', 'Type 2'])

# Extract the required columns
selected_columns = df[['Name', 'Type 1', 'Type 2']]

# Convert to JSON
result_json = selected_columns.to_json(orient='records')

# Save to a JSON file
output_file = "/Users/suare111803/Documents/PokeSudoku/pokemondata.json"
with open(output_file, 'w') as f:
    f.write(result_json)

# Get unique types from 'Type 1' and 'Type 2' columns
unique_types = set(df['Type 1'].unique()).union(set(df['Type 2'].unique()))

# Save unique types to a JSON file
types_output_file = "/Users/suare111803/Documents/PokeSudoku/unique_types.json"
with open(types_output_file, 'w') as f:
    json.dump(list(unique_types), f)



# Print the JSON (optional)
# print(result_json)