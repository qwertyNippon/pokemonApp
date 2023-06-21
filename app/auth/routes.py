from flask import Blueprint, render_template, request, redirect, url_for
from .forms import RegisterForm, LoginForm
from ..models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)

            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            user_name = form.username.data
            password = form.password.data
            print(user_name, password)

            user = User.query.filter_by(username=user_name).first()
            print(user)
            if user:
                print(user.password)
                if user.password == password:
                    print('you logged in!')
                else:
                    print('wrong!')
            else:
                print('that user doesn\'t exist')


            # .first() looks for the first query asked for.
            # user = db.session.execute(db.select(User).filter_by(username=user_name)) --> newer syntax
            # different version of the same use case.

    return render_template('login.html', form=form)