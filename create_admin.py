from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя')
    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем уже существует')
        sys.exit()
    password1 = getpass('Введите пароль')
    password2 = getpass('Введите пароль')
    if not password1 == password2:
        print('Пароли не совпадают')
        sys.exit()
    new_user = User(username=username, role='admin')
    new_user.set_password(password1)
    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))

