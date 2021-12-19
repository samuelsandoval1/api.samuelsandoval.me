from flask import Flask, jsonify, send_file
from os import path
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# / (main page)
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
    response = jsonify(About_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /education
@app.route("/education", methods=["GET"])
def education():
    Education_Text = {
        'text': '<strong class="header-name">California State University, Fullerton</strong><br>B.S. Computer Science, Expected Grad: May 2023'
    }
    response = jsonify(Education_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /experience


@app.route("/experience", methods=["GET"])
def experience():
    Experience_Text = {
        'text': '<strong class="header-name">Microsoft (May 2021)</strong><br><i>Incoming Explore Intern</i><br><strong class="header-name">Google (May 2020 - August 2020)</strong><br><i>STEP Intern</i>'
    }
    response = jsonify(Experience_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /hobbies
@app.route("/hobbies", methods=["GET"])
def hobbies():
    Hobbies_Text = {
        'hobby1': '- Making/Drinking Coffee Lattes <br>\ ',
        'hobby2': '- Doing lighting for concerts and churches. <br>\ ',
        'hobby3': '- Playing games like Minecraft with friends',
        'hobby4': '- Traveling to new places'
    }
    response = jsonify(Hobbies_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /projects
@app.route("/projects", methods=["GET"])
def projects():
    Projects_Text = {
        'project1': '<strong class="header-name">Sudoku GUI Solver</strong><br><i>A Sudoku Solver that uses the backtracking algorithm, and has a GUI to play sudoku. Built using Python, and pygame. View by typing /#sudoku-solver above in the domain.</i><br>\ ',
        'project2': '<strong class="header-name">TuffyHacks.com</strong><br><i> A web application designed to make ice breakers fun! Built with Next.JS and Web Sockets. View by typing /#Nicebreakers above in the domain.</i><br>\ ',
        'project3': '<strong class="header-name">Flix </strong><br><i>An iOS mobile application that allows users to browse movies now playing in theaters. Built with Xcode, Swift and the Movie Database API. View by typing /#Flix above in the domain </i><br>\ ',
        'project4': '<strong class="header-name">Personal API </strong><br><i> An API designed to display information about Samuel Sandoval. This website is fetching from this API. Built using Python and Flask. </i><br>',
    }
    response = jsonify(Projects_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /skills
@app.route("/skills", methods=["GET"])
def skills():
    Skills_Text = {
        'text': '<span class="code">Languages:</span> Design Thinking, Product Management, C++, Python, Swift, JavaScript, TypeScript, HTML, CSS, SQL',
    }
    response = jsonify(Skills_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

