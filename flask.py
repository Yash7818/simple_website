from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/registration'
db = SQLAlchemy(app)


'''
first_name,last_name,email
'''


class Registration_form(db.Model):
    first_name = db.Column(db.String(20), primary_key=True,  unique = False )
    last_name = db.Column(db.String(20) , unique = False)
    email = db.Column(db.String(30), unique = False)


@app.route('/')
def hello_world():
    return render_template('HOME_page.html')
@app.route('/yash')
def about():
    return render_template('new_login_page.html')
@app.route('/form', methods=['GET', 'POST'])
def kotlin():
    if (request.method=='POST') :
        first = request.form.get('first')
        last = request.form.get('last')
        email = request.form.get('email')

        entry = Registration_form(first_name=first, last_name=last, email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('registration_form.html')
@app.route('/password')
def password():
    return render_template('password.html')
@app.route('/username')
def username():
    return render_template('username.html')
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')
if __name__ == '__main__':
    app.run(debug= True)
    
   

    
 
