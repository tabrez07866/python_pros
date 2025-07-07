library={
    "available":{"DSA","Python","Math"},
    "issued":set()
}

def add_new_book(book):
    if book not in library["available"]:
        library["available"].add(book)
        print(f"new book '{book}' is added")
    else:
        print(f"book of '{book} already available'")

def issue_book(book):
    if book in library["available"]:
        library["available"].remove(book)
        library["issued"].add(book)
        print(f"📔 Book '{book}' issued")
    else:
        print("❌ Book not available or already issued")

def return_book(book):
    if book in library["issued"]:
        library["issued"].remove(book)
        library["available"].add(book)
        print(f"✅ Book '{book}' returned")
    else:
        print("❌ Book was not issued")

def show_status():
    print("Available: ",library["available"])
    print("Issued: ",library["issued"])
    
add_new_book("Chemistry")
issue_book("Chemistry")
return_book("Chemistry")
show_status()
