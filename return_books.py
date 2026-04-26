from utils import library

def return_book(book):
    if book in library:
        library[book] += 1
    else:
        library[book] = 1
    print(f"Returned 1 copy of '{book}'")