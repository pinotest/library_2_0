from app import app, db
from app.models import Author, Books, Shelf, association_table

from flask import Flask, render_template, request
from app.models import Author, Books, Shelf, association_table


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Author": Author,
        "Books": Books,
        "Shelf": Shelf,
        "association": association_table
    }


# @app.route('/library', methods=['GET'])
# def get_books_list():
#     """get books list"""
#     return render_template(
#         'books.html',
#         books=Books.query.all(),
#         title="Show Books"
#     )
