from app import app
from app import app, db
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
