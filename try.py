import flask
import flask_security
from flask import Flask, render_template
#import flask.ext.security
from flask_sqlalchemy import  SQLAlchemy
from  flask_bootstrap import Bootstrap
#from flask.ext.bootstrap
from flask_mail import Mail
from flask_security import UserMixin, RoleMixin


app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='file.sqlite:',
    #SECRET_KEY='James Bond',
    #SECURITY_REGISTERABLE=True,
)

db = SQLAlchemy(app)


Bootstrap(app)
Mail(app)
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(),
                                                db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

#user_datastore = flask_security.SQLAlchemyUserDatastore(db, User, Role)
#flask_security

"""
@app.before_first_request
def setupDatabase():
    db.create_all()
"""

""""""

@app.route('/')
def index():
    return render_template('index_alternative.html')


if __name__ == '__main__':
    app.run()
