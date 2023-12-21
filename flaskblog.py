from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)



app.config['SECRET_KEY'] = 'd2ae437c935bb147a852bbdf44827522'

posts = [
    {
        'Authors' : 'Michael Solomon',
        'Title' : 'Blog post1',
        'content' : 'First post Michael',
        'date_posted' : '23/02/23'
    },
    {
        'Authors' : 'Abiyu Nigussie',
        'Title' : 'Blog post2',
        'content' : 'First post of Abiyu',
        'date_posted' : '23/11/21'
    },
    {
        'Authors' : 'Mihret Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Mihret',
        'date_posted' : '12/12/19'
    }
]

@app.route("/")
@app.route("/home")
def Home():
    return render_template('Home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('About.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('Register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('Login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)