# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask.ext.login import logout_user, login_required
from manage import db
from ..email import send_email
from flask.ext.login import current_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('一封确认邮件已发送到您的邮箱')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

#login_required 修饰器会保护这个路由，因此，用户点击确认邮件中的
#链接后，要先登录，然后才能执行这个视图函数。
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirme(token):
        flash('成功确认你的账号。感谢！')
    else:
        flash('确认链接无效或已过期')
    return redirect(url_for('main.index'))

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '确认你的账户',
               'auth/email/confirm', user=current_user, token=token)
    flash('一封新的确认邮件已发送到您的邮箱.')
    return redirect(url_for('main.index'))

# 1.用户已登录 2.用户的账户还未确认。3.请求的端点不在认证蓝本中
# 如果请求满足以上3 个条件，则会被重定向到/auth/unconfirmed 路由，显示一个确认账户相关信息的页面。
# @auth.before_app_request
# def before_request():
#     if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.' and request.endpoint != 'static':
#         return redirect(url_for('main.index'))
#     return render_template('auth/unconfirmed.html')

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')












