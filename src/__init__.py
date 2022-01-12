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
@app.route('/help_message', methods=["GET"])
def help_message():
    Help_Text = {
        'text' : 'Supported commands: <span class="code">about</span>, <span class="code">education</span>,  <span class="code">experience</span>, <span class="code">the gospel</span>, <span class="code">projects</span>, <span class="code">clear</span>'
    }
    response = jsonify(Help_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
    return response


# /about
@app.route("/about", methods=["GET"])
def about():
    About_Text = {
        'text': " Hey there! <br> I'm an undergraduate student  studying Computer Science at California State University, Fullerton (CSUF). \
                I'm passionate about developing products and technologies that impact my community and people everywhere. <br><br> \
                At CSUF,  you can catch me doing some work in the TSU, hanging out in the ECS Courtyard or at my favorite coffee shop in Fullerton.  \
                I'm an active Executive Director of TuffyHacks, CSUF's premier student-run hackathon which focuses on uniting hackers to create technical solutions that solve real-world problems. \
                While I'm not on the grind, I'll sometimes travel around, make coffee lattes or hang out with friends. <br><br>\
                I love learning about new ideas, technology or experiences, so feel free to reach out to me. <br><br>\
                Let's <strong><a href='https://linkedin.com/in/~samuel/'>connect</a></strong><br><br> \
                <strong>Scroll up in the terminal.</strong>"
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


# /experience
@app.route("/gospel", methods=["GET"])
def the_gospel():
    Gospel_Text = {
        'header':'<strong class="header-name">The Gospel</strong><br><br>',
        'text': '<strong class="header-name">What does it mean to be a Christian?</strong><br> \
            Being a Christian is more than identifying yourself with a particular religion or affirming a certain value system. A Christian means you have embraced what the Bible says about God, mankind, and salvation. Consider the following truths found in Scripture.<br><br> \
            <strong class="header-name">God Is The Sovereign Creator</strong><br> \
           Contemporary thinking says man is the product of evolution but the Bible says we were created by a personal God to love, serve, and enjoy endless fellowship with Him. The New Testament reveals it was Jesus Himself who created everything (John 1:3; Colossians 1:16). Therefore, He also owns and rules everything (Psalm 103:19). That means He has authority over our lives and we owe Him absolute allegiance, obedience, and worship.<br> \
            <strong class="header-name">God Is Holy</strong><br> \
            God is absolutely and perfectly holy (Isaiah 6:3), therefore He cannot commit or approve of evil (James 1:13). God requires holiness of us. (1 Peter 1:16) says, “You shall be holy, for I am holy.” <br><br> \
            <strong class="header-name">Mankind Is Sinful</strong><br> \
            According to Scripture, everyone is guilty of sin: “There is no man who does not sin” (1 Kings 8:46). That doesn’t mean we’re incapable of performing acts of human kindness. but we’re utterly incapable of understanding, loving, or pleasing God on our own (Romans 3:10-12). <br><br>\
            <strong class="header-name">Sin Demands a Penalty</strong><br> \
            God’s holiness and justice demand that all sin be punished by death (Ezekiel 18:4). That’s why simply changing our patterns of behavior can’t solve our sin problem or eliminate its consequences. <br><br> \
            <strong class="header-name">Jesus Is Lord and Savior</strong><br> \
            The New Testament reveals it was Jesus Himself who created everything (Colossians 1:16). Therefore He owns and rules everything (Psalm 103:19). That means He has authority over our lives and we owe Him absolute allegiance, obedience, and worship. (Romans 10:9) says,” If you confess with your mouth Jesus as Lord, and believe in your heart that God raised Him from the dead, you shall be saved.” Even though God’s justice demands death for sin, His love has provided a Savior who paid the penalty and died for sinners (1 Peter 3:18). Christ’s death satisfied the demands of God’s justice and Christ’s perfect life satisfied the demands of God’s holiness (2 Corinthians 5:21), thereby enabling Him to forgive and save those who place their faith in Him (Romans 3:26).<br><br> \
            <strong class="header-name">Repentance: the Character of Saving Faith</strong><br> \
            True faith is always accompanied by repentance from sin. Repentance is agreeing with God that you are sinful, confessing your sins to Him, and making a conscious choice to turn from sin (Luke 13:3, 5; 1 Thessalonians 1:9), pursue Christ (Matthew 11: 28-30; John 17:3) and obey Him (1 John 2:3). It isn’t enough to believe certain facts about Christ. Even Satan and his demons believe in the true God (James 2:19), but they don’t love and obey Him. Saving faith is always accompanied by an increasing pattern of obedience (Ephesians 2:10).<br><br> \
            For more information, check out this <strong><a href="https://www.cru.org/us/en/train-and-grow/spiritual-growth/core-christian-beliefs/what-is-gospel/">resource</a></strong> <br><br> \
            <strong>Scroll up in the terminal.</strong>' 

    }
    response = jsonify(Gospel_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# /projects
@app.route("/projects", methods=["GET"])
def projects():
    Projects_Text = {
        'project1': '<strong class="header-name">TuffyHacks.com</strong><br>Product Manager<br><i> Lead a cross-functional team for the MVP development of the TuffyHacks.com. Some of my product work included: creating product requirements, communicating with stakeholders and translating requirements into user stories. TuffyHacks.com is a platform that allows hackers to have an interactive experience at the TuffyHacks hackathon. View <strong><a href="https://tuffyhacks.com">here</a></strong>.</i><br>',
        'project2': '<strong class="header-name">GP-Aide App </strong><br>Product Manager<br><i> Drove the MVP development with a team of other students. In this project, created product specs, managed the product sprint progress, and contributed to the technical development of the application. GP-Aide an iOS mobile application that allows users to calculate their semester grade point average. View <strong><a href="https://github.com/samuelsandoval1/223w-gp-aide">here</a></strong>.</i><br>',
        'project3': '<strong class="header-name">NiceBreakers </strong><br>Product Manager <br><i>Lead the product efforts to design product specs, create UX wireframes, and develop this idea into an MVP. Nicebreakers provides space for individuals to play games and get to know more about each other. View <strong><a href="https://devpost.com/software/nicebreakers-8hwuoe">here</a></strong>.</i><br>',
        'project4': '<strong class="header-name">Personal API </strong><br>Personal Project<br><i> An API designed to display information about Samuel Sandoval. This website is fetching from this API. Built using Python and Flask. View <strong><a href="http://github.com/samuelsandoval1/api.samuelsandoval.me">here</a></strong>.</i><br>',
        'project5': '<strong class="header-name">Flix </strong><br>Personal Project<br><i>An iOS mobile application that allows users to browse movies now playing in theaters. Built with Xcode, Swift and the Movie Database API. View <strong><a href="http://github.com/samuelsandoval1/Flix">here</a></strong>.</i><br><br>',
        'scroll':   '<b>Scroll up in the terminal.</b> '
    }
    response = jsonify(Projects_Text)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

