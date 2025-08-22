# File Read & Write Challenge with Error Handling

def modify_content(line):
    return line.upper()  # converting all text to uppercase

def main():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Open the input file in read mode
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Modify the content
        modified_lines = [modify_content(line) for line in lines]

        # Define output filename
        output_file = "modified_" + input_file

        # Open the output file in write mode
        with open(output_file, 'w') as f:
            f.writelines(modified_lines)

        print(f"Modified content has been written to '{output_file}' successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Cannot read/write the file. Check permissions or file status.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
