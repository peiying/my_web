# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask,render_template,session,url_for,redirect,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'ni cai'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(baseDir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name

if __name__ == '__main__':
    # role_admin = Role(name='Admin')
    # user_tom = User(username='tom',role=role_admin)
    # user_jim = User(username='jim',role=role_admin)
    # user_tim = User(username='tim',role=role_admin)
    # user_sam = User(username='sam',role=role_admin)
    # db.session.add(role_admin)
    # db.session.add(user_tom)
    # db.session.add(user_jim)
    # db.session.commit()

    for u in User.query.all():
        print u