from distutils.log import debug
from sympy import true
from flask import Flask,jsonify

app = Flask(__name__)

courses=[
    {
    'name':'Learn Ethical Hacking from Scratch',
    'instructor':'Zaid Shaikh',
    'completed':'20%',
    },
    {
        'name':'C Programming for Beginners-Master the C language',
        'instructor':'Jason Fedin',
        'completed':'100%'
    },
    {
        'name':'The Complete 2021 Flutter Development Bootcamp with Dart',
        'instructor':'Dr. Angela Yu',
        'completed':'30%'
    },
    {
        'name':'Python for Data Science and Machine Learning Bootcamp',
        'instructor':'Jose Portilla',
        'completed':'55%'
    },
    {
        'name':'Python for Data Structures, Algorithms, and Interviews!',
        'instructor':'Jose Portilla',
        'completed':'45%'
}
]

@app.route("/")

def index():
    return "First API"

@app.route("/courses",methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route('/courses/{name}',methods=['GET'])
def get_course(name):
    return jsonify({'course':courses[name]})  

if __name__== "__main__":
    app.run(debug=true)