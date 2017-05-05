# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


from flask import render_template,session,url_for,redirect,flash
from datetime import datetime
from flask.ext.login import login_required
from app.main.forms import NameForm
from manage import app


# baseDir = os.path.abspath(os.path.dirname(__file__))
#
# app = Flask(__name__)
# manager = Manager(app)
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# app.config['SECRET_KEY'] = 'ni cai'
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(baseDir,'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db = SQLAlchemy(app)
#
# class NameForm(FlaskForm):
#     name = StringField('你的名字?',validators=[DataRequired()])
#     submit = SubmitField('提交')

@app.route('/',methods=['GET', 'POST'])
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

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


#如果未认证的用户访问这个路由,Flask-Login 会拦截请求,把用户发往登录页面。
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

#if __name__ == "__main__":
    #manager.run('runserver')
    #app.run(debug=True, port=9999)
    #db.create_all()