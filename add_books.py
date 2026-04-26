from utils import library

def add_book(book, count):
    if book in library:
        library[book] += count
    else:
        library[book] = count
    print(f"Added {count} copies of '{book}'")