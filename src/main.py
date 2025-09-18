from books import add_book, list_books, search_book, update_stock, delete_book
from members import add_member, update_member_email, delete_member
from borrow import borrow_book, return_book

def main():
    while True:
        print("\n--- Library Management ---")
        print("1. Add book")
        print("2. List all books")
        print("3. Search books")
        print("4. Update book stock")
        print("5. Delete book")
        print("6. Add member")
        print("7. Update member email")
        print("8. Delete member")
        print("9. Borrow book")
        print("10. Return book")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            category = input("Category: ").strip()
            stock = int(input("Stock: ").strip())
            created = add_book(title, author, category, stock)
            print("Book added:", created)

        elif choice == "2":
            books = list_books()
            if books:
                for b in books:
                    print(f"{b['book_id']}: {b['title']} (Author: {b['author']}) - {b['category']} - Stock: {b['stock']}")
            else:
                print("No books found.")

        elif choice == "3":
            title = input("Enter title to search: ").strip()
            results = search_book(title)
            if results:
                for b in results:
                    print(f"{b['book_id']}: {b['title']} (Author: {b['author']}) - {b['category']} - Stock: {b['stock']}")
            else:
                print("No books found.")

        elif choice == "4":
            book_id = input("Book ID to update: ").strip()
            new_stock = int(input("New stock: ").strip())
            updated = update_stock(book_id, new_stock)
            print("Updated:", updated if updated else "Failed - check Book ID")

        elif choice == "5":
            book_id = input("Book ID to delete: ").strip()
            deleted = delete_book(book_id)
            print("Deleted:", deleted if deleted else "Cannot delete - book is borrowed or invalid ID")

        elif choice == "6":
            name = input("Member Name: ").strip()
            email = input("Member Email: ").strip()
            created = add_member(name, email)
            print("Member added:", created)

        elif choice == "7":
            name = input("Member Name to update: ").strip()
            new_email = input("New Email: ").strip()
            updated = update_member_email(name, new_email)
            print("Updated:", updated if updated else "Failed - check name")

        elif choice == "8":
            member_id = input("Member ID to delete: ").strip()
            deleted = delete_member(member_id)
            print("Deleted:", deleted if deleted else "Cannot delete - member has borrowed books or invalid ID")

        elif choice == "9":
            member_id = input("Member ID: ").strip()
            book_id = input("Book ID: ").strip()
            print(borrow_book(member_id, book_id))

        elif choice == "10":
            member_id = input("Member ID: ").strip()
            book_id = input("Book ID: ").strip()
            print(return_book(member_id, book_id))

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
