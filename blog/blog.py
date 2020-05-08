from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '704646bd9b607c04e365e4ec63be2502'

posts = [
    {
        'author': 'Biron Odhiambo',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 08, 2020'
    },
    {
        'author': 'Lovine Otieno',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 09, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def register():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)