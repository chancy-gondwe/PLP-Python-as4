def read_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Attempt to open the input file for reading
        with open(input_filename, "r") as infile:
            # Read the contents of the file
            content = infile.read()
            print("File read successfully!")
            
            # Modify the content (e.g., add a prefix to each line)
            modified_content = "\n".join(f"Modified: {line}" for line in content.splitlines())
            
            # Ask for the output filename
            output_filename = input("Enter the name of the file to write the modified content: ")
            
            # Write the modified content to the new file
            with open(output_filename, "w") as outfile:
                outfile.write(modified_content)
                print(f"Modified content successfully written to {output_filename}!")
                
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please ensure it is accessible.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
