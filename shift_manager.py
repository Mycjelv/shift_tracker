import os, sys, datetime
from flask import Flask, request, render_template, url_for, redirect
from flask_login import LoginManager, login_user, login_required
app = Flask(__name__)

usr=""
psd=""

def login_check():
    if usr != 'admin' or psd != 'admin':
        return redirect(url_for('login'))

@app.route('/')
def index():
    login_check()
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] != 'admin' or request.form['pswd'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            usr = request.form['uname']
            psd = request.form['pswd']
            return redirect(url_for())
    return render_template('login.html', error=error)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    login_check()
    return render_template('add_employee.html')

@app.route('/clock_in_out')
def clock_in_out():
    login_check()
    return render_template('clock_in_out.html')

@app.route('/schedule')
def schedule():
    login_check()
    return render_template('schedule.html')

@app.route('/active_manager')
def active_manager():
    login_check()
    return render_template('active_manager.html')


if __name__ == '__main__':
    app.run()