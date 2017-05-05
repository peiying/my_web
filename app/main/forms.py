# -*- coding: UTF-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')


from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email,DataRequired


class NameForm(Form):
    name = StringField('你的名字?',validators=[DataRequired()])
    submit = SubmitField('提交')