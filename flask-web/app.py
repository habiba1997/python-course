from flask import Flask, redirect, url_for, request, render_template
# lightwight database, file database
from flask_sqlalchemy import SQLAlchemy
import os

# __name__ it helps flask determine the location of our main application file
app = Flask(__name__)
print('name', __name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    is_active = True
    return render_template('profile.html', username=username, is_active=is_active)


@app.route('/profile/<int:id>')
def profile_id(id):
    return '<h1> This is profile page for the person with id %s </h1>' % id


@app.route('/request')
def request_data():
    return '<h1> Request Object %s </h1>' % request.headers


@app.route('/admin')
def welcome_admin():
    return '<h1> Welcome Admin </h1>'


@app.route('/guest/<guest>')
def welcome_guest(guest):
    return '<h1> Welcome Guest %s </h1>' % guest


@app.route('/user/<user>')
def welcome_user(user):
    if user == 'admin':
        return redirect(url_for('welcome_admin'))
    return redirect(url_for('welcome_guest', guest=user))


# setting up database
project_directory = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_directory, "mydatabase.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


# end database configuration
class Book(db.Model):
    # set name as table primary key
    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(100), nullable=False)


# Create the database tables
with app.app_context():
    print("create models....")
    db.create_all()


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/add-book')
def add_book():
    return render_template('add_book.html')


@app.route('/submit-book', methods=['POST'])
def submit_book():
    name = request.form['name']
    author = request.form['author']
    book = Book(name=name, author=author)
    db.session.add(book)
    db.session.commit()
    return redirect('/books')


@app.route('/update-books')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebooks.html', books=books)


@app.route('/update', methods=['POST'])
def update():
    oldname = request.form['oldname']
    name = request.form['newname']
    author = request.form['newauthor']
    book = Book.query.filter_by(name=oldname).first()
    book.name = name
    book.author = author
    db.session.commit()
    return redirect('/books')


@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['name']
    book = Book.query.filter_by(name=name).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/books')


# run in debug mode so every change i made is saved directly on browser
# The reloader and debugger is set to true
# => the job of reloder is to watch all those files for changess and when it notices that any one of te files changes
# it restart the server automatically
# debug mode to true, shows the error message in more details is returned
if __name__ == '__main__':
    app.run(debug=True)
