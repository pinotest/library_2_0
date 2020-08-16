from app import db

association_table = db.Table('association',
                             db.Column('Books', db.Integer,
                                       db.ForeignKey('books.id')),
                             db.Column('Author', db.Integer,
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
