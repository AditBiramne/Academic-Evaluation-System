from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="academic_evaluation"
)
cursor = db.cursor()

# Route for the home page
@app.route('/')
def index():
    return render_template('form.html')

# Route for submitting student data
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        roll_number = request.form['roll_number']
        semester_marks = request.form['semester_marks']
        assignment_grades = request.form['assignment_grades']
        
        # Store data in database
        sql = "INSERT INTO student_data (name, roll_number, semester_marks, assignment_grades) VALUES (%s, %s, %s, %s)"
        val = (name, roll_number, semester_marks, assignment_grades)
        cursor.execute(sql, val)
        db.commit()
        
        return "Data submitted successfully!"

# Route for administrators to view all student data
@app.route('/admin/students', methods=['GET'])
def admin_view_students():
    # Check if user is authenticated as administrator
    if not is_admin_authenticated():
        return redirect(url_for('login'))  # Redirect to login page if not authenticated
    
    # Retrieve all student data from the database
    all_student_data = retrieve_all_student_data()

    # Render an HTML template to display the data
    return render_template('admin_students.html', students=all_student_data)

def is_admin_authenticated():
    # Check if user is authenticated as administrator
    return session.get('admin')

def retrieve_all_student_data():
    # Retrieve all student data from the database
    cursor.execute("SELECT * FROM student_data")
    return cursor.fetchall()

if __name__ == '__main__':
    app.run(debug=True)
