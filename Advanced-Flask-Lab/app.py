from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    _name_,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.britannica.com%2F36%2F167236-050-BF90337E%2FEars-corn.jpg&tbnid=Zc1qE0w9Oop4aM&vet=12ahUKEwifiOSZuZyAAxXepycCHfEaAXwQMygCegUIARCOAg..i&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Fplant%2Fcorn-plant&docid=W1wJVxOqWU0Z7M&w=1600&h=1200&q=corn&ved=2ahUKEwifiOSZuZyAAxXepycCHfEaAXwQMygCegUIARCOAg"
user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."
aboutMe = "i am a very smart meet student"
posts = {
    "https://imageio.forbes.com/blogs-images/samarmarwan/files/2018/03/MEET-Students-1200x800.jpg": "Group projects <3",
    "https://uploads-ssl.webflow.com/5dd64bd3a930f96c82bd137a/63024ce64d943673cb004a4c_2022.07.17%20-%20Summer%20Day%201.png": "MEET summer!",
    "https://uploads-ssl.webflow.com/5dd64bd3a930f9d04abd1363/5de6d502d6d70c0ad49a060c_6.jpg": "#MEET_DU",
    "https://global-uploads.webflow.com/5fe28feebcae602620061802/5fe5401840671a36cd1d47d5_5de6d5024dd1a74670173aed_1-p-1080.jpeg": "Our lovely TAs!"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', user_bio = user_bio,
     image_link=image_link,posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html', aboutMe=aboutMe)


if _name_ == "_main_":  # Makes sure this is the main process
    app.run(debug=True)