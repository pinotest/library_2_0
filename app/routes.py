from app import app
from flask import Flask, render_template, request, redirect, url_for
from app.models import Author, Books, Shelf, association_table
from forms import BooksForm
from app.models import Library
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


@app.route('/library/', methods=['GET', 'POST'])
def get_books_list():
    """get books list"""
    form = BooksForm()
    logging.info('form %s' % form)
    logging.info('form.data %s' % form.data)
    if request.method == "POST":
        if form.validate_on_submit():
            Library.create_new_book(
                form.data['title'], form.data['type'], form.data['full_name'], form.data['status'])

        return redirect(url_for("get_books_list"))
    return render_template(
        'books.html',
        books=Books.query.all(),
        title="Show Books",
        form=form
    )
