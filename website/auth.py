
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user :
            if check_password_hash(user.password, password):
                flash('Login Success', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
                flash('Email does not exist.', category='error')
    return render_template("login.html", boolean=True, user= current_user)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def singup():
    if request.method == 'POST' :
        inputEmailAddress = request.form.get('inputEmailAddress')
        inputFirstName = request.form.get('inputFirstName')
        inputLastName = request.form.get('inputLastName')
        inputPassword = request.form.get('inputPassword')
        inputConfirmPassword = request.form.get('inputConfirmPassword')

        
        if len(inputFirstName) == 0:
             flash('First Name must fill.', category='error')
        elif len(inputLastName) == 0:
             flash('Last Name must fill.', category='error')
        elif len(inputEmailAddress) < 4 :
            flash('Email must be greater then 4 character.', category='error')
        elif inputPassword != inputConfirmPassword :
             flash('Password is not match.', category='error')
        elif len(inputPassword) < 6 :
             flash('Password must be greater then 6 character.', category='error')
        else:
            #add user to database
            new_user = User(email=inputEmailAddress, first_name=inputFirstName, password=generate_password_hash(
                inputConfirmPassword, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("signup.html", user=current_user)
