from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, Employee

routes = Blueprint('routes', __name__)

def validate_login(username, password):
    # Add logic to validate the username and password
    # This should return True if login is successful, False otherwise
    if username == 'admin' and password == 'password':  # Example credentials
        return True
    return False

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if validate_login(username, password):
            # Optionally store user information in session
            session['username'] = username
            return redirect(url_for('routes.homepage'))  # Redirect to homepage
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    
    return render_template('login.html')  # Render the login form for GET request

@routes.route('/homepage')
def homepage():
    return render_template('homepage.html')

@routes.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        salary = float(request.form['salary'])
        department = request.form['department']
        contact = request.form['contact']
        new_employee = Employee(name=name, salary=salary, department=department, contact=contact)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('routes.view_employees'))
    return render_template('add_employee.html')

@routes.route('/view_employees')
def view_employees():
    employees = Employee.query.all()
    return render_template('view_employees.html', employees=employees)

@routes.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    
    if request.method == 'POST':
        employee.name = request.form.get('name', employee.name)
        employee.salary = float(request.form.get('salary', employee.salary))
        employee.department = request.form.get('department', employee.department)
        employee.contact = request.form.get('contact', employee.contact)

        db.session.commit()
        return redirect(url_for('routes.view_employees'))
    
    return render_template('update_employee.html', employee=employee)



@routes.route('/delete_employee/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('routes.view_employees'))
