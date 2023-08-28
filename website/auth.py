from flask import Blueprint, Flask, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstname')
        lastName = request.form.get('lastname')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('Firstname must be greater than 2 characters', category='error')
        elif password != password2:
            flash('password must be match', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('Account created', category='success')

    return render_template("signup.html")
