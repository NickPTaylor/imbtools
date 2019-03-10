"""
Blueprint for authentication.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, \
                  request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app.models import IMBUser
from .forms import LoginForm

BP = Blueprint('auth', __name__)


@BP.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login.

    :return: Login page.
    :rtype: html
    """
    # Redirect to index if the user is already authenticated.
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = IMBUser.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully')

        # Make sure the next URL is a relative URL i.e. belongs to  this
        # site to mitigate open redirect attacks.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@BP.route('/logout')
def logout():
    """
    Logout.

    :return: Logout page.
    :rtype: html
    """
    logout_user()
    return redirect(url_for('auth.login'))
