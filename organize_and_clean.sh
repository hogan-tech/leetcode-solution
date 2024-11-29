#!/bin/bash

# Create destination folders if they don't exist
mkdir -p Python C++ TypesSript JavaScript SQL Readme

# Loop through all directories
for folder in */; do
    # Remove the trailing slash from the folder name
    folder_name=$(basename "$folder")
    
    # Move Python files to Python folder
    if [ -f "$folder/$folder_name.py" ]; then
        mv "$folder/$folder_name.py" Python/
    fi
    
    # Move TypeScript files to Typescript folder
    if [ -f "$folder/$folder_name.ts" ]; then
        mv "$folder/$folder_name.ts" TypeScript/
    fi
    
    # Move JavaScript files to JavaScript folder
    if [ -f "$folder/$folder_name.js" ]; then
        mv "$folder/$folder_name.js" JavaScript/
    fi

    # Move SQL files to SQL folder
    if [ -f "$folder/$folder_name.sql" ]; then
        mv "$folder/$folder_name.sql" SQL/
    fi

    # Move C++ files to C++ folder
    if [ -f "$folder/$folder_name.cpp" ]; then
        mv "$folder/$folder_name.cpp" C++/
    fi

    # Rename README.md to {foldername}.md and move to Readme folder
    if [ -f "$folder/README.md" ]; then
        mv "$folder/README.md" "Readme/${folder_name}.md"
    fi

    # Delete the folder if it is empty or contains only one NOTES.md
    if [ -d "$folder" ]; then
        contents=$(ls -A "$folder") # List all files in the folder
        if [ "$contents" == "NOTES.md" ] || [ -z "$contents" ]; then
            rm -rf "$folder"
        fi
    fi

done

echo "Files have been organized successfully, and original folders have been deleted!"
