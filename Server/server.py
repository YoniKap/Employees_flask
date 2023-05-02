from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import Client
import json
app = Flask(__name__,template_folder="../templates")

# Pass the required route to the decorator.
@app.route("/test")
def hello():
    return "Healthy"

@app.route('/Register_employee', methods=['GET','POST'])
def register_employee():
    if request.method == 'POST':
       Name= request.form.get('Name')
       Gender = request.form.get('Gender')
       Age = request.form.get('Age')
       ID = request.form.get('ID')
       Job = request.form.get('Job')
       Salary = request.form.get('Salary')
       sql=f" INSERT INTO  Employees ( name, gender , age , id , job , salary) VALUES  ({Name} , {Gender} , {Age} , {ID} , {Job} , {Salary})"
       newdata=json.dumps({"name": Name, "gender": Gender, "age": Age, "id": ID, "job": Job, "salary": Salary})

       return "<center><h1>New Employee Form Was Submitted Successfully!</h1>"\
              "<div>NAME: {} <br><br> GENDER: {} <br><br> AGE: {} <br><br> ID: {} <br><br> JOB: {} <br><br> " \
              "SALARY :{}</div> <br>json: {}<br>" \
              " SQL: {} </center>".format(Name,Gender,Age,ID,Job,Salary,newdata,sql)

    return render_template("Register.html")


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)










