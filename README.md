# Assignment 4: File Handling, Exceptions, and Errors in Python

This repository contains solutions for Module 5 of the Python programming module: Files, Exceptions, and Errors. The assignment includes two tasks that demonstrate reading, writing, appending, and handling file-related errors in Python.

---

## Task 1: Read a File and Handle Errors

`task1.py` reads a text file named `sample.txt` and prints its contents line by line. If the file does not exist, it displays a user-friendly error message.

### Expected Behavior

If the file exists:

```
Reading file content:

Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

If the file does not exist:

```
Error: The file 'sample.txt' was not found.
```

---

## Task 2: Write and Append Data to a File

`task2.py` asks the user to enter text and writes it to a file named `output.txt`. It then takes another user input and appends it to the same file. Finally, it reads and displays the final content of the file.

### Example Output

```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

---

## Folder Structure

```
├── task1.py
├── task2.py
├── sample.txt (optional for testing)
└── README.md
```


## Author

Jashandeep Singh

