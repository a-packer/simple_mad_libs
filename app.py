from flask import Flask, request, render_template
from random import choice
from stories import stories


app = Flask(__name__)

story = choice(stories)

prompts = story.prompts


@app.route('/')
def home_page():
    return render_template('mad_form.html', prompts=prompts)


@app.route('/story')
def show_story():
   
    user_story = story.generate(request.args)
    return render_template('story.html', user_story=user_story) 
