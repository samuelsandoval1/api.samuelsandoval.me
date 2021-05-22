from flask import Flask
from os import path
from flask import request
from flask import jsonify
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

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
        About_Text = {
            'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
             I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
        }
        return jsonify(About_Text)

    # /experience
    @app.route("/experience", methods=["GET"])
    def experience():
        About_Text = {
            'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
             I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
        }
        return jsonify(About_Text)
    # /hobbies
    @app.route("/about", methods=["GET"])
    def about():
        About_Text = {
            'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
             I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
        }
        return jsonify(About_Text)
    # /projects

    @app.route("/about", methods=["GET"])
    def about():
        About_Text = {
            'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
             I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
        }
        return jsonify(About_Text)
    # /skills

    @app.route("/about", methods=["GET"])
    def about():
        About_Text = {
            'text': " Hey there! 👋🏼 <br> \ I'm Sam, a sophomore studying Computer Science at California State University, Fullerton. \
             I love programming, building projects, and teaching others about new technologies. I'm interested in Developer Advocacy and Product Management."
        }
        return jsonify(About_Text)

    # 404

    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>404</h1><p>The resource could not be found.</p>", 404
    return app
