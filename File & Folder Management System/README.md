# File & Folder Management System

A command-line File & Folder Management System built in **Python**. It performs full **CRUD** (Create, Read, Update, Delete) operations on files and folders from a simple menu, without leaving the terminal.

## Features

**Folders**
- **Create** a new folder (with a check that it does not already exist)
- **Read** all files and folders, including those inside subfolders, as a numbered list
- **Update** (rename) an existing folder
- **Delete** a folder along with everything inside it

**Files**
- **Create** a file and write content into it
- **Read** and display the content of a file
- **Update** a file in three ways:
  - Rename the file
  - Append text to the existing content
  - Overwrite the entire content
- **Delete** a file

**General**
- Existence checks before every action (no overwriting by mistake when creating or renaming)
- Error handling with `try / except`, so the program does not crash on invalid input
- Menu runs in a loop until the user chooses to exit

## Tech Stack

- Python 3
- Standard library only: `pathlib`, `shutil`
- Concepts used: functions, loops, conditionals, file handling (`open` in read / write / append modes), exception handling, `Path` methods (`exists`, `is_file`, `is_dir`, `mkdir`, `rename`, `unlink`, `rglob`)

## Project Structure

```
File & Folder Management System/
├── main.py      # Program code and menu
└── README.md
```

## How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone the repository and open the project folder:
   ```bash
   git clone https://github.com/poojan9506/Python.git
   cd "Python/File & Folder Management System"
   ```
3. Run the program:
   ```bash
   python main.py
   ```

No external libraries need to be installed.

## Usage

When you start the program, this menu appears:

```
Options :-
1. Create a folder
2. Read files and folders
3. Update the folder
4. Delete the folder
5. Create a file
6. Read a file
7. Update a file
8. Delete a file
0. Exit the program
Please choose your option :-
```

Example flow:

1. Choose `1` and create a folder named `notes`
2. Choose `5` and create a file `notes/todo.txt` with some text
3. Choose `6` to read the file back
4. Choose `7` to append more text or rename the file
5. Choose `2` anytime to see everything in the current directory

## Important Note

The program works inside the **folder you run it from** (the current working directory).

- Option `2` lists everything in that location, including `main.py` itself.
- Option `4` deletes a folder **permanently along with all its contents**, with no recycle bin and no confirmation prompt. Use it carefully, and preferably test inside a separate practice folder.

## Future Improvements

- Confirmation prompt before deleting a folder
- Prevent accidental deletion or renaming of `main.py`
- Copy and move files between folders
- Search for files by name or extension
- Show file size and last modified date

## Author

**Poojan Desai**
- GitHub: [poojan9506](https://github.com/poojan9506)
- LinkedIn: [poojan-desai](https://linkedin.com/in/poojan-desai)
- Email: poojandesai06@gmail.com
