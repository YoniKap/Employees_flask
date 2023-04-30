class Employee:

    def __init__(self,name,gender,age,id,job,salary):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__id = id
        self.__job = job
        self.__salary = salary

    def __setName__(self,  name):
        self.__name=name
    def __getName__(self):
        return self.__name

    def __setGender__(self,  g):
        self.__gender = g
    def __getGender__(self):
        return self.__gender

    def __setAge__(self,  age):
        self.__age=age
    def __getAge__(self):
        return self.__age

    def __setID__(self,  id):
        self.__id = id
    def __getID__(self):
        return self.__id

    def __setJob__(self,  job):
        self.__job=age
    def __getJob__(self):
        return self.__job

    def __setSalary__(self,  salary):
        self.__salary=salary
    def __getSalary__(self):
        return self.__salary

    def __str__(self):
        return "{} {} {} {} ".format(self.__name,self.__age,self.__id,self.__job)





