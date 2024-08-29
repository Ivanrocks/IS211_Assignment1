class Book:
    """
    This class holds information about a book.

    Attributes:
        author: a string that contains the author of the book. Default is "".
        title: a string that contains the title of the book. Default is "".
    """
    def __init__(self,author = "" , title = "" ):
        """Initializes the attributes of the class"""
        self.author = author
        self.title = title

    def display(self):
        """Prints the phrase title, written by author"""
        print(f"{self.title}, written by {self.author}")



if __name__ == "__main__":
    Book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    Book2 = Book("Walter Scott", "Ivanhoe: A Romance")
    Book1.display()
    Book2.display()