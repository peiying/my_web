# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')


from . import main
from flask import render_template,session,url_for,redirect,flash
from datetime import datetime
from flask.ext.login import login_required
from .forms import NameForm

@main.route('/',methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        if name == session.get('name'):
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))
        else:
            flash('名字输入错误!')
    return render_template('index.html', current_time=datetime.utcnow(),form=form, name=session.get('name'))