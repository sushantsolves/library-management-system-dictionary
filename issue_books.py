from utils import library

def issue_book(book):
    if book in library and library[book] > 0:
        library[book] -= 1
        print(f"Issued 1 copy of '{book}'")
    else:
        print(f"Book '{book}' not available")