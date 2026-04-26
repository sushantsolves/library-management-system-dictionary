from utils import library

def show_books():
    if not library:
        print("\n")
        print("+----------------------------------+")
        print("|        LIBRARY IS EMPTY          |")
        print("+----------------------------------+")
    else:
        print("\n")
        print("+----------------------------------+")
        print("|        AVAILABLE BOOKS           |")
        print("+----------------------------------+")
        print("| Book Name           | Quantity   |")
        print("+----------------------------------+")
        for book, count in library.items():
            print(f"| {book[:18]:<18}  | {str(count):<10} |")
        print("+----------------------------------+")