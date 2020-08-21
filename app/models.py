from app import db
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

association_table = db.Table('association',
                             db.Column('book_id', db.Integer,
                                       db.ForeignKey('books.id')),
                             db.Column('author_id', db.Integer,
                                       db.ForeignKey('author.id'))
                             )


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    type = db.Column(db.String(200), index=True)
    author = db.relationship(
        "Author", secondary=association_table, back_populates="books")
    shelf = db.relationship("Shelf", backref="shelf", lazy="dynamic")

    def __str__(self):
        return f"<Books {self.title}>"


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(200), index=True, unique=True)
    books = db.relationship(
        "Books", secondary=association_table, back_populates="author")

    def __str__(self):
        return f"<Author {self.fullname}>"


class Shelf(db.Model):
    __tablename__ = 'shelf'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=1)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __str__(self):
        return f"<Author {self.fullname}>"


class Library:

    def get_books_list(self):
        join_books_author = Books.query.join(Author, Books.author).with_entities(
            Books.id, Books.title, Books.type, Author.fullname)
        return join_books_author

    def create_new_book(self, title, type, author_fullname, shelf_status):
        logging.info("title %s" % title)
        logging.info("type %s" % type)
        logging.info("author_fullname %s" % author_fullname)
        logging.info("shelf_status %s" % shelf_status)

        new_book = None
        book_main = Books(title=title, type=type)
        db.session.add(book_main)
        db.session.flush()
        book_author = Author(fullname=author_fullname)
        db.session.add(book_author)
        book_shelf = Shelf(status=shelf_status, book_id=book_main.id)
        db.session.add(book_shelf)
        # add relation book <=> author
        book_main.author.append(book_author)
        db.session.add(book_main)
        db.session.commit()
        new_book = True
        return new_book


library = Library()
