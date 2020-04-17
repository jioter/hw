import json
import random

from flask import Flask, render_template

app = Flask(__name__)


with open('movies.json') as f:
    MOVIES = json.load(f)


@app.route('/home')
def home_page():
    return render_template('home.html', title='Home')


@app.route('/movies')
def movies_page():
    return render_template('movies.html', title='Movies list', movies=MOVIES)


@app.route('/<title>')
def movie_page(title):
    for i, movie in enumerate(MOVIES):
        if MOVIES[i].get('title') == title:
            return render_template('movie.html', title=title, movie=MOVIES[i])
    return render_template('movies.html', title='Movies list', movies=MOVIES)


@app.route('/random_movie')
def random_movie():
    max_id = max([int(movie.get("id")) for movie in MOVIES])
    rnd_id = random.randint(0, max_id)
    return render_template('movie.html', movie=MOVIES[rnd_id])


if __name__ == '__main__':
    app.run(debug=True)
