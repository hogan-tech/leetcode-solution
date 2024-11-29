import re

def process_test_md(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    header = lines[:2]  # Retain the header and column names
    data = lines[2:]    # Process the rest of the data

    updated_data = []

    for line in data:
        columns = line.split('|')
        if len(columns) < 4:  # Skip empty or invalid rows
            continue
        
        # Process the Solution column
        solution = columns[3].strip()
        match_solution = re.search(r"\[(.*?)\]\(\./(.*?)/(.*?)\)", solution)
        if match_solution:
            language = match_solution.group(1)
            filename = match_solution.group(3)
            new_solution = f"[{language}](./{language}/{filename})"
            columns[3] = f" {new_solution} "

        # Process the Difficulty & ReadMe column
        difficulty_readme = columns[4].strip()
        match_readme = re.search(r"\[(.*?)\]\(\./(.*?)/README\.md\)", difficulty_readme)
        if match_readme:
            difficulty = match_readme.group(1)
            foldername = match_readme.group(2)
            new_readme = f"[{difficulty}](./Readme/{foldername}.md)"
            columns[4] = f" {new_readme} "

        updated_data.append('|'.join(columns))

    # Write the updated content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(header)
        file.writelines(updated_data)

# Specify the input and output file paths
input_file = 'test.md'
output_file = 'updated_test.md'

process_test_md(input_file, output_file)
