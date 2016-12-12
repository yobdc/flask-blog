#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'lr_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Post(db.Model):
    __tablename__ = 'lr_post'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.String(20))
    created_time = db.Column(db.DateTime)
    updated_time = db.Column(db.DateTime)
    title = db.Column(db.String(50))
    text = db.Column(db.Text(4294967295))


class Comment(db.Model):
    __tablename__ = 'lr_comment'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.String(20))
    created_time = db.Column(db.DateTime)
    text = db.Column(db.String(200))


class Remind(db.Model):
    __tablename__ = 'lr_remind'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.String(20))
    created_time = db.Column(db.DateTime)
    create_on_time = db.Column(db.DateTime)
    need_remind = db.Column(db.Boolean)
    text = db.Column(db.String(200))


def init_db():
    db.create_all()

    # 初始化用户
    user1 = User('admin1', 'admin1')
    user2 = User('admin2', 'admin2')
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()


def drop_db():
    db.drop_all()


if __name__ == '__main__':
    drop_db()
    init_db()
