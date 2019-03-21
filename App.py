from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector, hashlib

app = Flask(__name__)

# MySQL connection
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="flaskusers"
)

# Settings
app.secret_key = 'secretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/signup')
def Registro():
        return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signUp():
    if request.method == 'POST':
        user = request.form['user']
        name = request.form['name']
        password = request.form['password']
        confirm = request.form['confirmPassword']
        cur = mydb.cursor()
        if password == confirm:
                psw = hashlib.md5()
                psw.update(password.encode('utf-8'))
                cur.execute('INSERT INTO users (user, name, password) VALUES (%s, %s, %s)', (user, name, psw.hexdigest()))
                mydb.commit()
                flash('User created successfully')
                return redirect(url_for('Registro'))
        if password != confirm:
                flash('Password doesn´t match')
                return redirect(url_for('Registro'))
        

@app.route('/signin')
def signIn():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def methodSignin():
        if request.method == 'POST':
                user = request.form['user']
                password = request.form['password']
                

@app.route('/addClient')
def addClient():
    return 'Add Client'

@app.route('/editClient')
def editClient():
    return 'Edit Client'

@app.route('/deleteClient')
def deleteClient():
    return 'Delete Client'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)