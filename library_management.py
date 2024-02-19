# bugra murat - akbank python bootcamp

PATH_LIBRARY = r"C:\\Users\\lemon\\Desktop\\library.txt"
SPLITTER = ","


class Library:
    def __init__(self, file_path=PATH_LIBRARY):
        self.file_path = file_path
        try:
            # Open the file in "a+" mode, creating it if it doesn't exist
            self.file = open(self.file_path, "a+")
        except Exception as e:
            print(f"Error: Unable to open file {self.file_path}. Reason: {e}")

    def list_books(self):
        try:
            # Seek to the beginning of the file
            self.file.seek(0)
            # Read the contents of the file
            file_contents = self.file.read()
            # Add each line to a list using splitlines() method
            book_lines = file_contents.splitlines()

            if not book_lines:
                print("No books found.")
            else:
                print("List of Books:")
                for book_info in book_lines:
                    # Split the book information into name and author
                    name, author, first_release_date, number_of_pages = book_info.split(
                        SPLITTER)
                    print(f"Book: {name}, Author: {author}")
        except Exception as e:
            print(f"Error: Unable to list books. Reason: {e}")

    def add_book(self):
        try:
            # Check if the last line in the file is empty
            self.file.seek(0, 2)  # Move to the end of the file
            last_position = self.file.tell()

            if last_position > 0:
                self.file.seek(last_position - 1)
                last_char = self.file.read(1)

                if last_char != "\n":
                    # If the last line is not empty, add a newline
                    self.file.write("\n")

            # Ask user input for book details
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            release_year = input("Enter the first release year: ")
            num_pages = input("Enter the number of pages: ")

            # Create a string with book information
            book_info = f"{title}, {author}, {release_year}, {num_pages}"

            # Append the line to the file
            self.file.write(book_info + "\n")
            print("Book added successfully.")

        except Exception as e:
            print(f"Error: Unable to add book. Reason: {e}")

    def remove_book(self):
        try:
            # Ask user input for the book title to be removed
            title_to_remove = input(
                "Enter the title of the book to be removed: ")

            # Read the file contents and add books to a list
            self.file.seek(0)
            file_contents = self.file.read()
            book_lines = file_contents.splitlines()

            if not book_lines:
                print("No books found.")
                return

            # Find the index of the book to be deleted in the list
            book_index = None
            for i, book_info in enumerate(book_lines):
                if title_to_remove in book_info:
                    book_index = i
                    break

            if book_index is not None:
                # Remove the book from the list
                del book_lines[book_index]

                # Remove the contents of the books.txt
                self.file.truncate(0)

                # Add all elements of the list to the books.txt
                for book_info in book_lines:
                    self.file.write(book_info + "\n")

                print(
                    f"Book with title '{title_to_remove}' removed successfully.")
            else:
                print(f"Book with title '{title_to_remove}' not found.")

        except Exception as e:
            print(f"Error: Unable to remove book. Reason: {e}")

    def __del__(self):
        try:
            # Close the file when the object is deleted
            if hasattr(self, 'file') and self.file is not None:
                self.file.close()
                print(f"File {self.file_path} closed.")
        except Exception as e:
            print(f"Error: Unable to close file {self.file_path}. Reason: {e}")


lib = Library()

# Menu
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    try:
        # Ask user input for menu item
        choice = int(input("Enter your choice (1-4): "))

        # Using if-elif-else statement, check the user input
        if choice == 1:
            lib.list_books()
        elif choice == 2:
            lib.add_book()
        elif choice == 3:
            lib.remove_book()
        elif choice == 4:
            # Exit the loop and close the file
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Close the file when exiting the loop
del lib
