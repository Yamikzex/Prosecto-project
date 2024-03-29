import time
import os  # Import the os module to check file existence

def read_file(file_name):
    try:
        start_time = time.time()
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"\n Content of the file '{file_name}':\n{content}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time to read the file: {elapsed_time:.4f} seconds")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def write_file(file_name, content):
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Check if the file already exists
    if os.path.exists(file_name):
        print(f"The file '{file_name}' already exists. Please choose a different name.")
        return

    start_time = time.time()
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Content written to the file '{file_name}':\n{content}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time to write to the file: {elapsed_time:.4f} seconds")

def main():
    print("Welcome to the file reading and writing program in .txt format")
    
    while True:
        print("\nOptions:")
        print("1. Read a file")
        print("2. Write to a file")
        print("3. Exit")

        option = input("Enter the number of the option you want: ")

        if option == '1':
            file_name = input("Enter the name of the file to read (including the .txt extension): ")
            read_file(file_name)
        elif option == '2':
            file_name = input("Enter the name of the file to write (including the .txt extension): ")
            content = input("Enter the content to write to the file: ")
            write_file(file_name, content)
        elif option == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a correct option.")

if __name__ == "__main__":
    main()
