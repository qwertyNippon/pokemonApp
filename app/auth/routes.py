from flask import Blueprint, render_template, request, redirect, url_for
from .forms import RegisterForm
from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')
# auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='auth')

@auth.route('/register', methods=['GET', 'Post'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username, email, password)
            user.save_user()
            return redirect(url_for('auth.login'))


    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')