filename = "output.txt"

text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.\n")

print("Final content of output.txt:")
with open(filename, "r") as file:
    print(file.read())
