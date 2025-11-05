#Task 2
# Write and Append data to a file

# ask user to enter some data
data = input("Enter some data : ")
print("===================")
file = open("output.txt", "w")
file.write(data + "\n")
file.close()
print("\nData written to output.txt successfully!")

# now ask user to enter extra data to add
extra = input("Enter extra data to append: ")


file = open("output.txt", "a")
file.write(extra + "\n")
file.close()
print("Extra data appended successfully!\n")
print("======================")

print("Final contents of output.txt:\n")
file = open("output.txt", "r")
for line in file:
    print(line.strip())
file.close()
