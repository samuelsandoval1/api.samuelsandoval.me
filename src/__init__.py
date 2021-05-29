from flask import Flask
from os import path
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  return "<h1>samuelsandoval.me API</h1><p>This site is an API that allows users to learn more about Samuel Sandoval</p>"

# /about
@app.route("/about", methods=["GET"])
def about():
    About_Text = {
        'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
          I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
    }
    return jsonify(About_Text)

# /education
@app.route("/education", methods=["GET"])
def education():
    Education_Text = {
        'text': '<strong class="header-name">California State University, Fullerton</strong><br>B.S. Computer Science, Expected Grad: May 2023'
    }
    return jsonify(Education_Text)

# /experience
@app.route("/experience", methods=["GET"])
def experience():
    About_Text = {
        'text': '<strong class="header-name">Microsoft (May 2021)</strong><br><i>Incoming Explore Intern</i><br><strong class="header-name">Google (May 2020 - August 2020)</strong><br><i>STEP Intern</i>'
    }
    return jsonify(About_Text)

# /hobbies
@app.route("/hobbies", methods=["GET"])
def hobbies():
    Hobbies_Text = {
        'hobby1': '- Making/Drinking Coffee Lattes <br>\ ',
        'hobby2': '- Doing lighting for concerts and churches. <br>\ ',
        'hobby3': '- Playing games like Minecraft with friends',
        'hobby4': '- Traveling to new places'
    }
    return jsonify(Hobbies_Text)

# /projects
@app.route("/projects", methods=["GET"])
def projects():
    Projects_Text = {
        'project1': '<strong class="header-name">Sudoku GUI Solver</strong><br><i>A Sudoku Solver that uses the backtracking algorithm, and has a GUI to play sudoku. Built using Python, and pygame. View by typing /#sudoku-solver above in the domain.</i><br>\ ',
        'project2': '<strong class="header-name">NiceBreakers</strong><br><i> A web application designed to make ice breakers fun! Built with Next.JS and Web Sockets. View by typing /#Nicebreakers above in the domain.</i><br>\ ',
        'project3': '<strong class="header-name">Techish</strong><br><i>A web application to match students to mentors in tech. Built with HTML/CSS, TypeScript and Java Servlets. View by typing /#Techish above in the domain.</i><br>\ ',
        'project4': '<strong class="header-name">Flix </strong><br><i>An iOS mobile application that allows users to browse movies now playing in theaters. Built with Xcode, Swift and the Movie Database API. View by typing /#Flix above in the domain </i><br>\ ',
        'project5': '<strong class="header-name">Personal API </strong><br><i> An API designed to display information about Samuel Sandoval. This website is fetching from this API. Built using Python and Flask. </i><br>',        
    }
    return jsonify(Projects_Text)

# /skills
@app.route("/skills", methods=["GET"])
def skills():
    Skills_Text = {
        'text': '<span class="code">Languages:</span> C++, Python, Swift, JavaScript, TypeScript, HTML, CSS'
    }
    return jsonify(Skills_Text)

# 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
