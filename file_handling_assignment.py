# File creation
try:
    # Open the file in write mode
    with open("my_file.txt", "w") as file:
        # Write some text to the file
        file.write("Hello, PLP Community!\n")
        file.write("This is a Mark's test file.\n")
        file.write("Week 5\n")
except Exception as e:
    print(f"Error creating file: {e}")

# File reading and display
try:
    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        contents = file.read()
        # Display the contents on the console
        print(contents)
except Exception as e:
    print(f"Error reading file: {e}")

# File appending
try:
    # Open the file in append mode
    with open("my_file.txt", "a") as file:
        # Append some text to the file
        file.write("This is the first additional line.\n")
        file.write("And a second additonal line.\n")
        file.write("123\n")
except Exception as e:
    print(f"Error appending file: {e}")

# Error handling
try:
    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        contents = file.read()
        # Display the contents on the console
        print(contents)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"Other error: {e}")
finally:
    print("Thanks for the assignment.")