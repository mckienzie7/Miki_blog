from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2ae437c935bb147a852bbdf44827522'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(20), nullable=False, default='deafult.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"USER ('{self.username}', '{self.email}', '{self.img_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"POST ('{self.title}','{self.date_posted}')"
    
    







posts = [
    {
        'Authors' : 'Michael Solomon',
        'Title' : 'Blog post1',
        'content' : 'First post Michael',
        'date_posted' : '23/02/23'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
        'date_posted' : '12/12/19'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
        'date_posted' : '12/12/19'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
        'date_posted' : '12/12/19'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
        'date_posted' : '12/12/19'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
        'date_posted' : '12/12/19'
    },
    {
        'Authors' : 'Eskedar Welday',
        'Title' : 'Blog post3',
        'content' : 'First post of Eskedar',
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

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' Account created for { form.username.data } !','success')
        return redirect(url_for('Home'))
    return render_template('Register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'Michaelelsa12@gmail.com' and form.password.data == '12345':
            flash("You have been logged in, succesfully", 'success')
            return redirect(url_for('Home'))
        else:
            flash('Login Unsuccessful check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)