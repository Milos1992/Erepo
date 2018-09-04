class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}


    def get_email(self):
        return self.email(User)

    def change_email(self, address):
        old_email = self.email
        self.email = address
        print("{name}'s email address ({old_email}) was changed for '{new_email}'".format(name = self.name, old_email = old_email, new_email = self.email))


    def __repr__(self):
        self.repre_string = ("User" + self.name + " " + ", email :" + self.email + " " + " , books read:" + str(len(self.books)))
        return self.repre_string

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user_email:
            return True
        else:
            return False

    def read_book (self, book, rating="None"):
        self.user_books[book] = rating

    def get_average_rating (self, book):
         self.book = book
         avrage_rate = 0
         for values in self.book.values():
             avrage_rate += float((sum(values)) / ((len(values))))
         return avrage_rate








class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = str(isbn)
        self.ratings = []


    def get_title(self, title):
            return self.title(Book)
    def get_isbn(self, isbn):
            return str(self.isbn(Book))
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("The book's isbn has been updated")

    def get_rating(self, rating):
           if 4>= rating >= 0:
               return self.ratings.append(rating)
           else:
               return "Invalid Rating"
    def __eq__ (self, other_book):
           if (Book.title == other_book.title ) and (str(Book.isbn ) == str(other_book.isbn)):
               return True
           else:
               return False


    def get_average_rating (self, ratings):
        self.ratings = ratings
        if sum(self.ratings) > 0:
            return round(sum(self.rating) / len(self.rating), 2)
        else:
            return 0

    def	__hash__(self):
          return	hash((self.title,	self.isbn))


class Fiction(Book):
    def __init__ (self, title, author, isbn):
        super().__init__(title, isbn)
        if author:
            self.author = author
    def get_author(self, author):
        return self.author
    def __repr__ (self):
        self.repr_book = "{title} by {author}".format(title=self.title, author=self.author)
        return self.repr_book

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn )
        self.subject = subject
        self.level = level
    def get_subject(self, subject):
        return self.subject
    def get_level(self, level):
        self.level = level
        return self.level
    def __repr__(self):
        self.repres_string2 = "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
        return self.repres_string2



class TomeRater():
    def __init__(self):
        self.users = {}
        self.users_books = {}


    def create_book (self, title , isbn):
        self.title = title
        self.isbn = isbn
        return Book(title,isbn)


    def create_novel (self, title, author , isbn):
        self.author = author
        self.title = title
        self.isbn = isbn
        if type(author)!= str:
            return Fiction(title,isbn)
        else:
            return Fiction(title,author, isbn)

    def create_non_fiction (self, title, subject, level, isbn) :
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user (self, book, name, email, rating="None"):
        self.email = email
        if email not in self.users:
                return  ("No user with email  + {email} + !".format(email = self.email ))
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.user_books:
                self.user_books[book] += 1
            else:
                self.user_books[book] = 1

    def add_user(self, name, email, user_books="None"):
        self.name = name
        self.email = email
        self.user_book = user_books
        user = User(name, email)
        self.users[user.email] = user
        if user_books is not None:
            if user_books is list:
                for i in user_books:
                    return  self.add_book_to_user(i, email, None)

    def print_catalog (self, user_books):
        self.books = user_books
        for book  in self.user_book.keys():
            return book
    def print_users (self, users):
        self.users = users
        for user  in self.users.values():
            return user

    def most_read_book(self, user_books, book ):
        self.books = user_books
        most = []
        most = max(self.user_books)
        return most
    def highest_rated_book (self, user_books, book):
        self.books = user_books
        high = []
        high = max(book.get_average_rating())
        return high
    def most_positive_user (self, users, user):
        self.users = users
        the_most = []
        the_most = max(user.get_average_rating())
        return the_most
