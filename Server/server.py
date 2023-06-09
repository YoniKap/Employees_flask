from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import csv

url = "http://127.0.0.1:5000"
order='SELECT * FROM employees ORDER BY name ASC'



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
    notexist=True
    cur = mysql.connection.cursor()
    cur.execute("SELECT id From employees;")
    check = cur.fetchall()
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
       return render_template("RegisterSucess.html", Name=Name, Gender=Gender, Age=Age, ID=ID, Job=Job, Salary=Salary,check=check,url=url)

    return render_template("Register.html",check=check,url=url)







@app.route("/Show_employee_list", methods=['GET','POST'])
def showemplist():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employees ORDER BY name ASC')
    data = cur.fetchall()

    if request.method == 'POST' :

        if 'name' in request.form:
             name = request.form['name']
             if name.isspace() or name == '':
                 cur.execute(order)
             else:
                 cur.execute(f"SELECT * FROM employees WHERE name = '{name}'")
             data = cur.fetchall()

        # If the form is submitted with an ID input, retrieve the ID from the form data
        elif 'id' in request.form:
             id = str(request.form['id'])
             if id == '':
                 cur.execute(order)
             else:
                 cur.execute(f"SELECT * FROM employees WHERE id = '{id}'")
             data = cur.fetchall()

        elif 'delete' in request.form:
            delete = str(request.form['delete'])
            cur.execute(order)
            cur.execute(f"DELETE FROM employees WHERE id = '{delete}'")
            mysql.connection.commit()

        elif 'orderbyjob' in request.form:
            cur.execute('select * from employees order by job ASC')
            data = cur.fetchall()

        elif 'orderbysalary' in request.form:
            cur.execute('SELECT * FROM employees ORDER BY salary DESC;')
            data = cur.fetchall()

    return render_template('showemployees.html', data=data)



@app.route("/showsalarystats",methods=['GET','POST'])
def showsalarystats():
    cur = mysql.connection.cursor()
    cur.execute(' SELECT job, AVG(salary) AS average_salary FROM employees GROUP BY job;')
    info = cur.fetchall()

    if request.method == 'POST' :

        if 'job' in request.form:
             job = request.form['job']
             if job.isspace() or job == '':
                 cur.execute(order)
             else:
                 cur.execute(f"SELECT job, AVG(salary) AS average_salary FROM employees WHERE job = '{job}' GROUP BY job;")
                 info = cur.fetchall()

    return render_template('salarystats.html',data=info)



@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html",url=url)


if __name__ == "__main__":
    app.run(debug=True)










