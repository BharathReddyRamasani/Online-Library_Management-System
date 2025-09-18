from config import sb

# CRUD for members
def add_member(name, email):
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

def update_member_email(name, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("name", name).execute()
    return resp.data

def can_delete_member(member_id):
    resp = sb.table("borrow_records").select("*").eq("member_id", member_id).execute()
    return not resp.data

def delete_member(member_id):
    if can_delete_member(member_id):
        resp = sb.table("members").delete().eq("member_id", member_id).execute()
        return resp.data
    return None
