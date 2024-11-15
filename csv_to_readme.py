import pandas as pd
import os
import csv
import chardet



def convert_csvs_to_readme(csv_files, output_file="README.md"):
    with open(output_file, "w") as readme:
        for csv_file in csv_files:
            # Get the filename without the extension and convert it to uppercase
            file_name = os.path.splitext(os.path.basename(csv_file))[0].upper()

            with open(csv_file, "rb") as f:
                result = chardet.detect(f.read())
                encoding = result['encoding']
            
            # Add the filename as a heading
            readme.write(f"# {file_name}\n\n")
            
            
            # Read the CSV file into a DataFrame
            try :
                df = pd.read_csv(
                    csv_file
                    , sep=","
                    , on_bad_lines="skip"
                    ,encoding= encoding
                    )
            except pd.errors.ParserError as e:
                print("Error while parsing the CSV:", e)
            
            # Convert the DataFrame to a Markdown table
            markdown_table = df.to_markdown(index=False)
            
            # Write the Markdown table to the README
            readme.write(markdown_table + "\n\n")
    
    print(f"Markdown tables saved to {output_file}")

# Example usage
csv_files = ["7seg(LED).csv", "adc.csv", "Attenuator.csv"]  # Add your CSV file names here
convert_csvs_to_readme(csv_files)