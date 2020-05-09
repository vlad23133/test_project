from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.users import users
from datetime.datetime import now


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run()


@app.route('/')
def index:
    session = db_session.create_session()
    ans = []
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    main()
