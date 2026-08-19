from pathlib import Path
import shutil

def create_folder():
  try:
    name = input("Please tell your folder name :- ")
    p = Path(name)
    p.mkdir()
    print("Folder created successfully")
  except Exception as err:
    print(f"Sorry, an error occurred: {err}")

def read_file_folder():
  p = Path("")
  items = list(p.rglob('*'))
  for i, v in enumerate(items):
    print(f"{i + 1} : {v}")

def update_folder():
  try:
    read_file_folder()
    old_name = input("Please tell which folder you want to update :- ")
    p = Path(old_name)
    if p.exists() and p.is_dir():
      new_name = input("Please tell your new folder name :- ")
      new_p = Path(new_name)
      p.rename(new_p)
      print("Your folder name was updated successfully")
    else:
      print("Sorry, no such folder exists")
  except Exception as err:
    print(f"An error occurred: {err}")

def delete_folder():
  try:
    read_file_folder()
    name = input("Please tell which folder you want to delete :- ")
    p = Path(name)
    if p.exists() and p.is_dir():
      shutil.rmtree(p)
      print("Folder deleted successfully")
    else:
      print("No such folder exists")
  except Exception as err:
    print(f"There was an error: {err}")

def create_file():
  try:
    read_file_folder()
    name = input("Please tell your file name :- ")
    p = Path(name)
    if not p.exists():
      with open(name, "w") as fs:
        data = input("Write what you want in this file :- ")
        fs.write(data)
      print("File created successfully")
    else:
      print("Sorry, a file with this name already exists")
  except Exception as err:
    print(f"An error occurred: {err}")

def read_file():
  try:
    read_file_folder()
    name = input("Please tell your file name :- ")
    p = Path(name)
    if p.exists() and p.is_file():
      with open(name, 'r') as fs:
        content = fs.read()
        print("Your file content is :- ")
        print(content)
    else:
      print("Sorry, no such file exists")
  except Exception as err:
    print(f"An error occurred: {err}")
    
def update_file():
  try:
    read_file_folder()
    name = input("Please tell your file name :- ")
    p = Path(name)
    if p.exists() and p.is_file():
      print("Options :- ")
      print("1. For renaming the file")
      print("2. For appending something to the file")
      print("3. For overwriting the file content")
      choice = int(input("Tell your choice :- "))

      if choice == 1:
        new_name = input("Tell your new name with extension :- ")
        new_p = Path(new_name)
        if not new_p.exists():
          p.rename(new_p)
          print("Your file name was changed successfully")
        else:
          print("Sorry, this name already exists")

      if choice == 2:
        with open(name, 'a') as fs:
          data = input("What do you want to append :- ")
          fs.write(" " + data)
        print("Data appended successfully")

      if choice == 3:
        with open(name, 'w') as fs:
          data = input("What do you want to overwrite :- ")
          fs.write(data)
        print("Data changed successfully")
  except Exception as err:
    print(f"An error occurred: {err}")

def delete_file():
  try:
    read_file_folder()
    name = input("Tell your file name with extension :- ")
    p = Path(name)
    if p.exists() and p.is_file():
      p.unlink()
      print("File deleted successfully")
    else:
      print("Sorry, no such file exists")
  except Exception as err:
    print(f"An error occurred: {err}")

while True:
  print("Options :- ")
  print("1. Create a folder")
  print("2. Read files and folders")
  print("3. Update the folder")
  print("4. Delete the folder")
  print("5. Create a file")
  print("6. Read a file")
  print("7. Update a file")
  print("8. Delete a file")
  print("0. Exit the program")  

  choice = int(input("Please choose your option :- "))

  if choice == 0:
    print("Program exited successfully")
    break

  if choice == 1:
    create_folder()

  if choice == 2:
    read_file_folder()

  if choice == 3:
    update_folder()

  if choice == 4:
    delete_folder()

  if choice == 5:
    create_file()

  if choice == 6:
    read_file()

  if choice == 7:
    update_file()

  if choice == 8:
    delete_file()
