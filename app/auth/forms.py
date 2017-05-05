# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email,DataRequired, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

#用户注册表单
class RegistrationForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, '
                                                           'numbers, dots or underscores')])
    password = PasswordField('密码', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])

    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

