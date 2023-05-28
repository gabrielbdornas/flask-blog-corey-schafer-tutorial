from flask import (
                   Flask,
                   render_template,
                   )

app = Flask(__name__)

posts = [
          {
          'author': 'Gabriel Dornas',
          'title': 'Blog Post 1',
          'content': 'First post content.',
          'date': 'May 28, 2023'
          },
          {
          'author': 'Corey Shafer',
          'title': 'Blog Post 2',
          'content': 'Second post content.',
          'date': 'May 29, 2023'
          },
          {
          'author': 'Paul McCartney',
          'title': 'Blog Post 3',
          'content': 'Third post content.',
          'date': 'May 30, 2023'
          },
]

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About')