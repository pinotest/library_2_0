from app import app
from flask import Flask, render_template, request
from app.models import Author, Books, Shelf, association_table
from forms import BooksForm


@app.route('/library', methods=['GET'])
def get_books_list():
    """get books list"""

    form = BooksForm()
    return render_template(
        'books.html',
        books=Books.query.all(),
        title="Show Books",
        form=form
    )
