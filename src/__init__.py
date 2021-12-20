from flask import Flask, jsonify, send_file
from os import path
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# / (main page)
@app.route('/')
def home():
  return "<h1>samuelsandoval.me API</h1><p>This site is an API that allows users to learn more about Samuel Sandoval</p>"

# /help
@app.route('/help_message')
def help_message():
    Help_Text = {
        'text' : 'Supported commands: <span class="code">about</span>, <span class="code">education</span>,  <span class="code">experience</span>, <span class="code">projects</span>, <span class="code">clear</span>'
    }
    response = jsonify(Help_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# /about
@app.route("/about", methods=["GET"])
def about():
    About_Text = {
        'text': " Hey there! 👋🏼 <br> I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
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
        'text': '<strong class="header-name">Microsoft (May 2021 - August 2021)</strong><br><i>Explorer Intern</i><br><strong class="header-name">Google (May 2020 - August 2020)</strong><br><i>STEP Intern</i>'
    }
    response = jsonify(Experience_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# /projects
@app.route("/projects", methods=["GET"])
def projects():
    Projects_Text = {
        'project1': '<strong class="header-name">TuffyHacks.com</strong><br>Product Manager Lead<br><i> Lead the product efforts to develop a hacakthon participant portal. This portal allows hackers to learn more about TuffyHacks and have a positive hackathon experience. View by typing /#TuffyHacks above in the domain.</i><br>',
        'project2': '<strong class="header-name">GP-Aide App </strong><br>Product Manager Lead<br><i>Designed product specs and led the product efforts and design and develop an iOS mobile application that allows users to calculate their semester grade point average. View by typing /#GPAide above in the domain.</i><br>',
        'project3': '<strong class="header-name">Personal API </strong><br>Personal Project<br><i> An API designed to display information about Samuel Sandoval. This website is fetching from this API. Built using Python and Flask. View by typing /#API above in the domain.</i><br>',
        'project4': '<strong class="header-name">Flix </strong><br>Personal Project<br><i>An iOS mobile application that allows users to browse movies now playing in theaters. Built with Xcode, Swift and the Movie Database API. View by typing /#Flix above in the domain.</i><br>',
    }
    response = jsonify(Projects_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

