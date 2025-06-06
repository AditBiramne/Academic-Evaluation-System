# Academic-Evaluation-System

🎓 Academic Evaluation System
This is a Flask-based web application designed to evaluate and manage student academic performance. It provides separate interfaces for students and administrators to input, view, and manage academic data.

📁 Project Structure
<pre> ```academic-evaluation-system/
│
├── app.py # Main Flask application: routes, logic, and DB interaction
│
├── static/
│ └── css/
│ └── styles.css # Custom CSS styles
│
├── templates/
│ ├── admin_students.html # Admin dashboard to manage student data
│ ├── form.html # Form for student mark submission
│ └── login.html # Login page'''</pre>
🚀 Features
Student login and data entry form

Admin panel to view and manage student performance

Evaluation based on academic inputs (UT marks, semester grades, etc.)

Clean and responsive UI using custom CSS

🧠 How it Works
app.py is the core of the application. It:

Initializes the Flask app

Defines routes for:

/login – User login

/form – Student mark entry

/admin – Admin dashboard

Handles form submissions and redirects

Connects to the database to store and fetch data

Renders HTML templates using render_template()

🛠️ Tech Stack
Backend: Flask (Python)

Frontend: HTML, CSS

Templating: Jinja2

Database: [Add MySQL / SQLite details here]

🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/academic-evaluation-system.git
cd academic-evaluation-system
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Configure the Database
Create your database (MySQL / SQLite)

Update credentials in app.py (or config.py if separated)

Initialize tables manually or via a provided script

4. Run the Application
bash
Copy
Edit
python app.py
📈 Future Enhancements
🔍 Add student performance prediction using ML

📄 Export results as PDF / Excel

🛡️ Role-based access control (Admin, Teacher, Student)

📊 Integration with Power BI dashboards
