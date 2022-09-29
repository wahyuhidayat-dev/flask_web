
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True, data=data)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET','POST'])
def singup():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        repeatpassword = request.form.get('repeatpassword')

        if len(email) < 4 :
            flash('Email must be greater then 4 character.', category='error')
        elif len(firstname) < 2:
             flash('First Name must be greater then 2 character.', category='error')
        elif len(lastname) < 2:
             flash('Last Name must be greater then 2 character.', category='error')
        elif password != repeatpassword :
             flash('Password is not match.', category='error')
        elif len(password) < 6 :
             flash('Password must be greater then 6 character.', category='error')
        else:
            #add user to database
             flash('Account Created.', category='success')
    return render_template("signup.html")

