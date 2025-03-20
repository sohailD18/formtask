from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'form_db'

mysql = MySQL(app)

# File Upload Config
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.form
    first_name = data['first_name']
    dob = data['dob']
    age = data['age']
    gender = data['gender']
    email = data['email']
    password = data['password']
    phone = data['phone']
    state = data['state']
    courses = data['courses']

    # Handle File Upload
    photo = request.files['photo']
    if photo:
        filename = secure_filename(photo.filename)
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        photo.save(photo_path)
    else:
        filename = None

    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO users (first_name, dob, age, gender, email, password, phone, state, courses, photo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (first_name, dob, age, gender, email, password, phone, state, courses, filename))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        dob = request.form['dob']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        state = request.form['state']
        courses = request.form['courses']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE users 
            SET first_name=%s, dob=%s, age=%s, gender=%s, email=%s, phone=%s, state=%s, courses=%s 
            WHERE id=%s
        """, (first_name, dob, age, gender, email, phone, state, courses, id))

        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('index'))  # Redirect back to the main page after update

@app.route('/edit/<int:id>')
def edit_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('edit.html', user=user)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
