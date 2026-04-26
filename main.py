from add_books import add_book
from issue_books import issue_book
from return_books import return_book
from show_books import show_books

def print_header():
    print("="*50)
    print("   !     WELCOME TO LIBRARY SYSTEM     !   ")
    print("="*50)


def print_footer():
    print("="*50)
    print("!       LIBRARY CLOSED - THANK YOU      !")
    print("="*50)


def print_menu():
    print("\n")
    print("+----------------------------------+")
    print("|            MAIN MENU             |")
    print("+----------------------------------+")
    print("| 1. Add Book                      |")
    print("| 2. Issue Book                    |")
    print("| 3. Return Book                   |")
    print("| 4. Show Books                    |")
    print("| 5. Exit                          |")
    print("+----------------------------------+")


print_header()

while True:
    print_menu()
    

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter book name: ").upper()
        count = int(input("Enter number of copies: "))
        add_book(name, count)

    elif choice == '2':
        name = input("Enter book name to issue: ").upper()
        issue_book(name)

    elif choice == '3':
        name = input("Enter book name to return: ").upper()
        return_book(name)

    elif choice == '4':
        show_books()

    elif choice == '5':
        print_footer()
        break

    else:
        print("Invalid choice, try again!")