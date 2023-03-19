from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    grade = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Student(name={self.name}, email={self.email}, grade={self.grade})"


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        grade = request.form['grade']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        student = Student(name=name, email=email, grade=grade,
                          gender=gender, address=address, phone=phone)
        try:
            db.session.add(student)
            db.session.commit()
            return render_template('/')
        except:
            return "ERROR"
    else:
        return render_template('create.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
