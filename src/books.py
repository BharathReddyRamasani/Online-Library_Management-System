from config import sb

# CRUD for books
def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data

def list_books():
    resp = sb.table("books").select("*").order("book_id", desc=False).execute()
    return resp.data

def search_book(title):
    resp = sb.table("books").select("*").ilike("title", f"%{title}%").execute()
    return resp.data

def update_stock(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data

def can_delete_book(book_id):
    resp = sb.table("borrow_records").select("*").eq("book_id", book_id).execute()
    return not resp.data

def delete_book(book_id):
    if can_delete_book(book_id):
        resp = sb.table("books").delete().eq("book_id", book_id).execute()
        return resp.data
    return None
