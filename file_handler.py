def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the name and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
