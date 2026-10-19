# Library Management System

A command-line Library Management System built in **Python**. It lets a librarian add books, register members, and track which member has borrowed or returned which book. All data is stored in a local JSON file, so nothing is lost when the program closes.

## Features

- **Add books** with title, author and number of copies
- **List all books** with total and available copies
- **Add members** with name and email
- **List members** along with the books each one has currently borrowed
- **Borrow a book**: checks that the member and book exist and that a copy is available
- **Return a book**: choose which borrowed book to return, and its copy count is restored
- **Unique IDs** auto-generated for books (`B-xxxxx`) and members (`M-xxxxx`)
- **Timestamps** saved for when a book was added or borrowed
- **Input validation** for invalid numbers, wrong IDs and zero-copy requests
- **Persistent storage** in `library.json`, created automatically on first run

## Tech Stack

- Python 3
- Standard library only: `json`, `random`, `string`, `pathlib`, `datetime`
- Concepts used: classes and objects, `@classmethod` / `@staticmethod`, file handling, list comprehensions, exception handling

## Project Structure

```
Library Management System/
├── main.py        # Program code and menu
├── library.json   # Data file (books and members)
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
   cd "Python/Library Management System"
   ```
3. Run the program from inside this folder (so `library.json` is found):
   ```bash
   python main.py
   ```

No external libraries need to be installed.

## Usage

When you start the program, a menu appears:

```
==================================================
Library Management System
==================================================
1. Add Book
2. List Books
3. Add Member
4. List Members
5. Borrow Book
6. Return Book
0. Exit the Portal
--------------------------------------------------
What task do you want to perform :-
```

Typical flow:

1. Add a book (option 1) and note its generated ID
2. Add a member (option 3) and note the member ID
3. Borrow a book (option 5) using the member ID and book ID
4. Check the member's borrowed books (option 4)
5. Return the book (option 6)

## Data Format

Data is saved in `library.json` in this structure:

```json
{
    "books": [
        {
            "id": "B-QmwLz",
            "title": "Book1",
            "author": "BookAuthor1",
            "total_copies": 25,
            "available_copies": 23,
            "added_on": "2026-08-24 11:40:25"
        }
    ],
    "members": [
        {
            "id": "M-Tf4Gq",
            "name": "Person1",
            "email": "person1@gmail.com",
            "borrowed": [
                {
                    "book_id": "B-QmwLz",
                    "title": "Book1",
                    "borrow_on": "2026-08-24 11:43:04"
                }
            ]
        }
    ]
}
```

## Future Improvements

- Search books by title or author
- Due dates and late-fee calculation
- Delete or update books and members
- Prevent the same member from borrowing the same book twice
- Move storage from JSON to a database (SQLite / PostgreSQL)

## Author

**Poojan Desai**
- GitHub: [poojan9506](https://github.com/poojan9506)
- LinkedIn: [poojan-desai](https://linkedin.com/in/poojan-desai)
- Email: poojandesai06@gmail.com
