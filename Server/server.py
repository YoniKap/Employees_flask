from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import csv





app = Flask(__name__,template_folder="../templates")
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB']='EmployeesApp'
mysql = MySQL(app)
# Pass the required route to the decorator.








@app.route("/test")
def hello():
    return "Healthy"








@app.route('/Register_employee', methods=['GET','POST'])
def register_employee():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
       Name= request.form.get('Name')
       Gender = request.form.get('Gender')
       Age = request.form.get('Age')
       ID = request.form.get('ID')
       Job = request.form.get('Job')
       Salary = request.form.get('Salary')
       sql = f"INSERT INTO EmployeesApp.employees (name, id, gender, job, salary, age) VALUES ('{Name}', '{ID}', '{Gender}', '{Job}', '{Salary}', '{Age}')"
       cur.execute(sql)
       mysql.connection.commit()
       newdata=json.dumps({"name": Name, "gender": Gender, "age": Age, "id": ID, "job": Job, "salary": Salary})

       return render_template("RegisterSucess.html", Name=Name, Gender=Gender, Age=Age, ID=ID, Job=Job, Salary=Salary)

    return render_template("Register.html")







@app.route("/Show_employee_list", methods=['GET','POST'])
def showemplist():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employees ORDER BY name ASC')
    data = cur.fetchall()
    if request.method == 'POST' :
        if 'name' in request.form:
             name = request.form['name']
             cur.execute(f"SELECT * FROM employees WHERE name = '{name}'")
             data = cur.fetchall()
        # If the form is submitted with an ID input, retrieve the ID from the form data
        elif 'id' in request.form:
             id = request.form['id']
             cur.execute(f"SELECT * FROM employees WHERE id = {id}")
             data = cur.fetchall()
        elif 'delete' in request.form:
            delete = request.form['delete']
            cur.execute(f"DELETE FROM employees WHERE id = {delete}")
            mysql.connection.commit()
        elif 'orderbyjob' in request.form:
            id= request.form['id']
            cur.execute('select * from employees order by job ASC')
            data = cur.fetchall()

    return render_template('showemployees.html', data=data)







@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)










