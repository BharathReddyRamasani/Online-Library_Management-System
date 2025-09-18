
📚 Library Management System (Python + Supabase)

A simple Library Management System built with Python and Supabase (PostgreSQL backend).
It allows managing books, members, and borrowing records with proper constraints (e.g., cannot delete borrowed books or members with borrowed books).

🚀 Features
✅ Books
Add new books (add_book)
Update book stock (update_stock)
Delete book (only if not borrowed)
List all books
Search books by title/author/category

✅ Members
Register new members (add_member)
Update member info (e.g., email)
Delete member (only if no borrowed books)
Show member details with borrowed books

✅ Borrow & Return
Borrow a book (borrow_book)
(decreases stock, creates a borrow record)
Return a book (return_book)
(increases stock, updates borrow record)

📂 Project Structure
LibraryManagement/
├── .env              # Supabase credentials
├── requirements.txt  # Dependencies
├── README.md         # Documentation
└── src/
    ├── config.py     # Supabase client setup
    ├── books.py      # Book operations
    ├── members.py    # Member operations
    ├── borrow.py     # Borrow/return operations
    └── main.py       # CLI entry point

📌 Notes

Members cannot be deleted if they still have borrowed books.
Books cannot be deleted if they are currently borrowed.
Borrowing automatically decreases stock, returning increases stock.

🛠 Tech Stack
Python 3.10+
Supabase (PostgreSQL)
Supabase-py client
dotenv for secrets