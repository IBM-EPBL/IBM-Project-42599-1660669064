from flask import Flask,render_template, request, url_for, flash, redirect
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mvc69919;PWD=V6lMd9Cej5H1oQOU",'','')
print(conn)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM students WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('list.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO students VALUES (?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, password)

      ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Student Data saved successfuly..")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/forgot")
def forgot():
    return render_template('forgot.html')

@app.route("/dashboard")
def dashbord():
    return render_template('dashboard.html')

@app.route("/wallet")
def wallet():
    return render_template('wallet.html')

@app.route("/expenses")
def expenses():
    return render_template('expenses.html')

@app.route("/email")
def email():
    return render_template('email.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')
