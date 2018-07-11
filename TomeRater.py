"""
Author: Gabriella Quattrone
Date Created: Sunday, July 8, 2018
Date Finished: Monday, July 9, 2018
"""
# The User class keeps track of users
class User:
    def __init__(self, name, email):
        # name and email are strings, while books is a dictionary.
        self.name = name
        self.email = email
        # Maps Book to User's Rating
        self.books = {} 
        
    # Returns email associated with user.
    def get_email(self):
        return self.email

    # Takes in new email address to replace old user's email address
    def change_email(self, address):
        # address is a string like email
        self.email = address
        print("User {} has had their email updated.".format(self.name))

    # Records a book that the user read.
    def read_book(self, book, rating = None):
        self.books[book] = rating

    # Gets user's average rating for books read.
    def get_average_rating(self):
        total = 0
        num_rated = 0
        # For a Book
        for value in self.books.values():
            if value:
                total += value
                num_rated += 1
        avg = total / num_rated
        return avg

    # Provides us data about the user.
    def __repr__(self):
        return """User: {} 
Email: {} 
Books Read: {}
              """.format(self.name, self.email, len(self.books))

    # Tells us if two users are the same.
    def __eq__(self, other_user):
        # If two users have the same name and email, they're identical
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

# The Book class defines books that have their own titles, isbns, and ratings for Users
class Book:
    def __init__(self, title, isbn):
        # title is a string, isbn is a number, ratings is a list
        self.title = title
        self.isbn = isbn
        self.ratings = []

    # Return the title of the book.
    def get_title(self): 
        return self.title

    # Return the ISBN of the book.
    def get_isbn(self):
        return self.isbn

    # Takes in a new ISBN and sets it as the book's
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{} had its ISBN updated to {}.".format(self.title, self.isbn))

    # Adds ratings that are from 0 - 4
    def add_rating(self, rating=None):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        elif rating == None:
            pass
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        avg = 0
        # Iterate through values and calculate average
        for rating in self.ratings:
            avg += rating
        try:
            avg = avg / len(self.ratings)
        except ZeroDivisionError:
            pass
        return avg
        print("\n")

    # Makes Book hashable for dictionary use
    def __hash__(self):
        return hash((self.title, self.isbn))

    # Provides us data about the user.
    def __eq__(self, other_book):
        # If two books have the same title and ISBN, they're identical
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return self.title

# The Fiction class is a subclass of Book and defines fiction books.
class Fiction(Book):
    def __init__(self, title, author, isbn):
        # Calls the __init__ of its parent class, Book
        Book.__init__(self, title, isbn)
        # author is a string
        self.author = author

    # Returns the author of a fictional book.
    def get_author(self):
        return self.author

    # Returns the title and author of a fictional book.
    def __repr__(self):
        return "{} by {}".format(self.title, self.author) 

# The Non-Fiction class is a subclass of Book and defines non-fiction books.
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        # Calls the __init__ of its parent class, Book
        Book.__init__(self, title, isbn)
        # subject and level are strings
        self.subject = subject
        self.level = level

    # Returns subject of a non-fiction book.
    def get_subject(self):
        return self.subject

    # Returns reading level of a non-fiction book.
    def get_level(self):
        return self.level

    # Returns information (such as the level and subject) of a non-fiction book
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

# The TomeRater class lets our Users and Books interact!
class TomeRater:
    def __init__(self):
        # Maps a user's email to the corresponding user
        self.users = {}
        # Maps a Book object to the number of Users that have read it
        self.books = {}

    # Creates a new book with given title and ISBN
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        print(new_book, "was created with ISBN {}.".format(isbn))
        return new_book

    # Creates a new fiction novel with given title, author and ISBN
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        print(new_fiction, "was created with ISBN {}.".format(isbn))
        return new_fiction

    # Creates a new non-fiction book with given title, subject, level and ISBN
    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        print(new_non_fiction, "was created with ISBN {}.".format(isbn))
        return new_non_fiction

    # Adds a book to the user's portfolio
    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        # Search by email for user
        if user:  
            user.read_book(book, rating)
            book.add_rating(rating)
            # We can also keep track of if other people read this book
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1      
        # This means we haven't found the matching user to the email
        else:
            print("No user with email", email)

    # Creates a new User and adds any Books
    def add_user(self, name, email, books = None):
        self.users[email] = User(name, email)
        # If there are books to be added, add them
        if books:
            # Iterate through books and add them to user's portfolio
            for book in books:
                self.add_book_to_user(book, email, None)

    # Prints all books.
    def print_catalog(self):
        # For formatting purposes
        print("\nCatalog")
        print("-------")
        # Iterates through all books and prints each one
        for book in self.books.keys():
            print(book)
        print("\n")

    # Prints all users.
    def print_users(self):
        # For formatting purposes
        print("Current Users")
        print("-------------")
        # Iterates through all users and prints each one
        for user in self.users.values():
            print(user)
        print("-------------")

    # Returns the most read book.
    def get_most_read_book(self):
        # Keep track while iterating by using a counter
        max_reads = 0
        most_read = None
        # Compare the value to the counter
        for book in self.books:
            num_reads = self.books[book]
            # Change counter to highest value found so far
            if num_reads > max_reads:
                max_reads = num_reads
                most_read = book
        # Return book with corresponding value
        return most_read

    # Returns the book with the highest average rating.
    def highest_rated_book(self):
        # Keep track while iterating by using a counter
        highest_rating = 0
        best_book = None
        # Compare the value to the counter
        for book in self.books: 
            avg = book.get_average_rating()
            # Change counter to highest rating found so far
            if avg > highest_rating:
                highest_rating = avg
                best_book = book
        # Return the book corresponding to the rating
        return best_book

    # Return user with highest average rating
    def most_positive_user(self):
        # Keep track while iterating by using a counter
        highest_rating = 0
        nicest_user = None
        
        # Compare the value to the counter
        for user in self.users.values():
            avg = user.get_average_rating()
            # Change counter to highest value found so far
            if avg > highest_rating:
                highest_rating = avg
                nicest_user = user
        # Return the corresponding user
        return nicest_user
