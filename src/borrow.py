from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
sb: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def borrow_book(member_id, book_id):
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    if not member:
        return f"Member ID {member_id} does not exist."
    book = sb.table("books").select("stock, title").eq("book_id", book_id).execute().data
    if not book:
        return f"Book ID {book_id} does not exist."
    if book[0]["stock"] <= 0:
        return f"Book '{book[0]['title']}' is out of stock."
    sb.table("borrow_records").insert({
        "member_id": member_id,
        "book_id": book_id,
        "borrow_date": datetime.now().isoformat()
    }).execute()

    sb.table("books").update({"stock": book[0]["stock"] - 1}).eq("book_id", book_id).execute()
    return f"Borrowed '{book[0]['title']}' successfully."

def return_book(member_id, book_id):
    record = sb.table("borrow_records").select("*")\
        .eq("member_id", member_id).eq("book_id", book_id).execute().data
    if not record:
        return "No borrow record found."
    sb.table("borrow_records").delete().eq("member_id", member_id).eq("book_id", book_id).execute()
    book = sb.table("books").select("stock, title").eq("book_id", book_id).execute().data
    sb.table("books").update({"stock": book[0]["stock"] + 1}).eq("book_id", book_id).execute()
    return f"Returned '{book[0]['title']}' successfully."
