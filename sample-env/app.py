# Day 6 Tasks

from flask import Flask
from flask import jsonify

app = Flask(__name__)

student = {
    "1" : "Vamsi",
    "2" : "Aishwarya",
    "3" : "Samantha"
    }

@app.route('/')
def helloWorld():
    return 'Hello! World'

@app.route('/students/all')
def getAllStudents():
    return student

@app.route('/jsonify')
def jsonContent():
    return jsonify(Id = 1,
    Name = student["1"])

@app.route('/students/<id>')
def getStudentById(id):
    return jsonify(Name = student[id])