#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, session, redirect, url_for, request
from models import db, app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    if (request.path != '/'
        and not '/api' in request.path
        and not request.path.endswith('.js')
        and not request.path.endswith('.css')
        and not request.path.endswith('.jpg')
        and not request.path.endswith('.png')
        and not session.has_key('username')):
        return redirect(url_for('index'))


@app.route("/family")
def family():
    return render_template('family.html')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
