
import pandas as pd

def csv_to_markdown(csv_file_path, columns_needed):
    # Load the CSV file
    bom_df = pd.read_csv(csv_file_path)

    # Selecting the specified columns
    bom_selected = bom_df[columns_needed]

    # Converting to GitHub Markdown table format
    return bom_selected.to_markdown(index=False)

# Example usage
csv_file_path = 'BOM.csv'  # Replace with your CSV file path
columns_needed = ['Reference', 'Value', 'Digikey', 'Price', 'Qty']  # Adjust columns as needed
markdown_table = csv_to_markdown(csv_file_path, columns_needed)
print(markdown_table)
