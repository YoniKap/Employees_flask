import requests
import Employee
isOpen=True

# requestdic = {
#                  0: testServer(),
#                  1: addEmployee,
#                  2: getEmployeeByID,
#                  3: getEmployeeByName,
#                  4: updateEmployee,
#                  5: deleteEmployee,
#                  6: getAllEmployees,
#                  7: importEmployeesFromCSV,
#                  8: exportEmployeesFromCSV,
#                  9: exit
#               }

def main():
  while(isOpen):
   what = int(input())

def testServer():
    print(requests.get("http://127.0.0.1:5000/test").text)

def addEmployee(name,gender,age,id,job,salary):
    emp = Employee(name,gender,age,id,job,salary)

def getEmployeeByID():
    pass

def getEmployeeByName():
    pass

def updateEmployee():
    pass

def deleteEmployee():
    pass

def importEmployeesFromCSV():
    pass

def exportEmployeesFromCSV():
    pass

def getAllEmployees():
    pass






if __name__ == "__main__":
    main()

