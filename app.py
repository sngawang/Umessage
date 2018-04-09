from flask import Flask, render_template, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['DEBUG'] = True
db = SQLAlchemy(app)

POSTGRES = {
    'user': 'user',
    'pw': 'password',
    'db': 'umessage',
    'host':'umessage.c8hjgod3jjwy.us-east-1.rds.amazonaws.com',
    'port': '5432'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s:%(port)s/%(db)s' %POSTGRES
db.init_app(app)

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))


# generate hash password for Users
    def set_password(self, password):
            self.password_hash = generate_password_hash(password)
#check if user's hash matches it
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == 'POST':
        username = request.form['username']
        if username not in Users.query.all():
            user_data = Users(
                usersname=request.form['username'],
                email = request.form['email'],
                name=request.form['name'])
            user_data.set_password(request.form['password'])
            db.session.add(register)
            db.session.commit()
        else:
            return "error"
        return render_template("signup.html")
    return render_template("index.html")

@app.route("/signup", methods=["POST","GET"])
def signup():
    """
    form = RegisterForm()

    if form.validate_on_submit():
#hashing password before storing into the db
        new_user = Users(username=form.username.data, email=form.email.data, password=form.password.data, name=form.name.data)
        db.session.add(new_users)
        db.commit()
        return " hello welcome"
"""
    return render_template("signup.html")
@app.route("/signedup")
def signedup():
    return render_template("signup.html")


if __name__ == '__main__':
        app.run()
        db.create_all()
