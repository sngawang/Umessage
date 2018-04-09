from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

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
if __name__ == '__main__':
    app.run()
    db.create_all()
