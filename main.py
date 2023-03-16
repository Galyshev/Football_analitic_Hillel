import os
from BD.alchemy import db_session
from flask import Flask, request, render_template, redirect, flash
from BD import Model_db
from flask import session as flsk_sess
import celery_work

flask_app = Flask(__name__)
flask_app.secret_key = os.environ.get("SECRET_KEY")

@flask_app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@flask_app.route("/Register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':

        return render_template('register.html')
    else:
        user = request.form['login']
        password = request.form['psw']
        email = request.form['email']

        insert_query = Model_db.Users(user=user, password=password, email=email)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()
        return render_template('register_ok.html')
@flask_app.route("/Login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', start=True)
    else:
        user_form = request.form['login']
        password_form = request.form['psw']
        query_login = db_session.query(Model_db.Users).filter_by(user=user_form)
        chk_login = ''
        chk_password = None
        for i in query_login:
            chk_login = i.user
            chk_password = i.password
        if chk_login == '':
            return render_template('login.html', no_login=True)
        if chk_password == password_form:
            flsk_sess['username'] = chk_login
            return render_template('update.html')
        else:
            return render_template('login.html', no_password=True)
@flask_app.route("/Logout", methods=['GET'])
def logout():
    if 'username' in flsk_sess:
        flsk_sess.pop('username', None)
        return render_template('index.html')
    else:
        return "Вы не авторизированы"

@flask_app.route("/Analytics", methods=['GET', 'POST'])
def analytics():
    if request.method == 'GET':
        # Если кто то вводит эндпоинт вручную, минуя авторизацию
        if 'username' in flsk_sess:
            #oбновление данных через selery
            celery_work.data_update()
            return render_template('analytics.html')
        else:
            return render_template('login.html')
    else:
        if 'username' in flsk_sess:
            pass

if __name__ == '__main__':
    flask_app.run(debug=True, host="0.0.0.0", port=5000)