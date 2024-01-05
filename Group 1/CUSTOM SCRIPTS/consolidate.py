import os
import pandas as pd

# Specify the directory where your CSV files are located
directory = 'test\CSVs'

# Create an empty DataFrame to store the consolidated data
consolidated_data = pd.DataFrame(columns=['prod_rev_imgs'])  # Create a single column DataFrame

# Loop through the CSV files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)

        # Read each CSV file into a DataFrame
        data = pd.read_csv(file_path)

        # Consolidate rows into a single column and add it to the consolidated DataFrame
        consolidated_data = pd.concat([consolidated_data, data.apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)], ignore_index=True)

# Specify the path for the consolidated CSV file
output_file = 'test/CONSOLIDATED.csv'

# Save the consolidated data to a new CSV file
consolidated_data.to_csv(output_file, index=False)

print("Consolidation complete. Data saved to", output_file)
