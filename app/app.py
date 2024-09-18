from flask import Flask, request, render_template, redirect, url_for, session, flash
from models import db, Employee
from routes import routes as routes_blueprint

app = Flask(__name__)
app.secret_key = 'secret_key'

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register blueprint
app.register_blueprint(routes_blueprint)

# Initialize database
with app.app_context():
    db.create_all()

# Dummy credentials for login (for testing)
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('routes.homepage'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
