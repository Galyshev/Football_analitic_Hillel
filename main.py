import os
from BD.alchemy import db_session
from flask import Flask, request, render_template, redirect
from BD import Model_db
from flask import session as flsk_sess
import celery_work
from analytics import create_analytics_content

flask_app = Flask(__name__)
flask_app.secret_key = os.environ.get("SECRET_KEY")

@flask_app.route("/", methods=['GET'])
def index():
    title = 'Вітання'
    return render_template('index.html', title=title)

@flask_app.route("/Register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        title = 'Реєстрація'
        return render_template('register.html', title=title)
    else:
        title = 'Реєстрація'
        user = request.form['login']
        password = request.form['psw']
        email = request.form['email']

        insert_query = Model_db.Users(user=user, password=password, email=email)
        db_session.add(insert_query)
        db_session.commit()
        db_session.close()
        return render_template('register_ok.html', title=title)
@flask_app.route("/Login", methods=['GET', 'POST'])
def login():
    title = 'Логін'
    if request.method == 'GET':
        return render_template('login.html', start=True, title=title)
    else:
        title = 'Логін'
        user_form = request.form['login']
        password_form = request.form['psw']
        query_login = db_session.query(Model_db.Users).filter_by(user=user_form)
        chk_login = ''
        chk_password = None
        for i in query_login:
            chk_login = i.user
            chk_password = i.password
        if chk_login == '':
            return render_template('login.html', no_login=True, title=title)
        if chk_password == password_form:
            flsk_sess['username'] = chk_login
            return render_template('update.html')
        else:
            return render_template('login.html', no_password=True, title=title)
@flask_app.route("/Logout", methods=['GET'])
def logout():
    title = 'logout'
    if 'username' in flsk_sess:
        flsk_sess.pop('username', None)
        return render_template('index.html', title=title)
    else:
        return "Вы не авторизированы"
@flask_app.route("/Update", methods=['GET'])
def update():
    title = 'Update'
    # oбновление данных через selery
    create_analytics_content.analytics_content_country()
    # celery_work.data_update()     #TODO обновление
    return redirect("/Analytics")
@flask_app.route("/Analytics", methods=['GET', 'POST'])
def analytics():
    title = 'Аналітика'
    if request.method == 'GET':
        if 'username' in flsk_sess:
            request_ranking_club = create_analytics_content.ranking_club()

            return render_template('analytics.html', title=title, request_ranking_club=request_ranking_club)
        else:
            title = 'Логін'
            return render_template('login.html', title=title)
    else:
        if 'username' in flsk_sess:
            return "Включился метод POST"

if __name__ == '__main__':
    flask_app.run(debug=True, host="0.0.0.0", port=5000)