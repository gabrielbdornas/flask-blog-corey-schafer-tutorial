from flask import (
                   Flask,
                   render_template,
                   url_for,
                   flash,
                   )
from forms import (
                   RegistrationForm,
                   LoginForm,
                   )

app = Flask(__name__)
app.config['SECRET_KEY'] = '76ce9b71a7bb3360dfc5af8083732a8e'

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

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data.title()}!', 'success')
    return redirect(url_for('home')) # home is the name of the function
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)