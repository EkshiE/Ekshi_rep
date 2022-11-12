""" Starting flask"""

from flask import render_template

from settings import app
from settings import HOST
from settings import PORT
from settings import DEBUG

from models import Student


@app.route('/')
def index():
    students = Student.query.all
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
