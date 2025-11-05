# Task 1 -Read a file and handle error

try :
    file = open("sample.txt","r")
    print(file.read())

    # read and print each line
    for line in file:
        print(line.strip())
        file.close()

except FileNotFoundError:
    print("The file 'sample.txt' does not exist.")

except Exception as e:
    # Handle any other unexpected error
    print(f"An unexpected error occurred: {e}")
