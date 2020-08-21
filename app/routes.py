from app import app
from flask import Flask, render_template, request, redirect, url_for
from app.models import Author, Books, Shelf, association_table
from forms import BooksForm
from app.models import library
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


@app.route('/library/', methods=['GET', 'POST'])
def get_books_list():
    """get books list"""
    form = BooksForm()
    if request.method == "POST":
        if form.validate_on_submit():
            library.create_new_book(
                form.data['title'], form.data['type'], form.data['full_name'], form.data['status'])
        return redirect(url_for("get_books_list"))
    return render_template(
        'books.html',
        books=library.get_books_list(),
        title="Show Books",
        form=form
    )
