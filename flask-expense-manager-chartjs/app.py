from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# setting up database
project_directory = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_directory, "expenses.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


# end database configuration
class Expense(db.Model):
    # set name as table primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)


# Create the database tables
with app.app_context():
    print("create models....")
    db.create_all()


@app.route('/')
def homepage():
    expenses = Expense.query.all()
    t_food, t_entertainment, t_business, t_other, total = calculate_total(expenses)
    return render_template('expense-information-form.html', expenses=expenses,
                           total=total, t_other=t_other, t_business=t_business, t_entertainment=t_entertainment
                           , t_food=t_food)


def calculate_total(expenses):
    t_food = 0
    t_entertainment = 0
    t_business = 0
    t_other = 0
    total = 0
    for exp in expenses:
        total += exp.amount
        if exp.category == 'food':
            t_food += exp.amount
        elif exp.category == 'entertainment':
            t_entertainment += exp.amount
        elif exp.category == 'business':
            t_business += exp.amount
        else:
            t_other += exp.amount

    return t_food, t_entertainment, t_business, t_other, total


@app.route('/add-expense', methods=['POST'])
def add():
    date = request.form['date']
    name = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']
    expense = Expense(date=date, name=name, amount=amount, category=category)
    db.session.add(expense)
    db.session.commit()
    return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    expense = Expense.query.filter_by(id=id).first()
    expense.date = request.form['date']
    expense.name = request.form['expensename']
    expense.amount = request.form['amount']
    expense.category = request.form['category']

    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    expense = Expense.query.filter_by(id=id).first()
    db.session.delete(expense)
    db.session.commit()
    return redirect('/')


@app.route('/edit/<int:id>')
def edit_expense(id):
    expense = Expense.query.filter_by(id=id).first()
    return render_template('edit-expense.html', expense=expense)


if __name__ == '__main__':
    app.run(debug=True)
