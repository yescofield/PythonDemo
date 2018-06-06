#!usr/bin/python
# -*- coding:UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        '计算员工总数'
        print "员工总共有" , Employee.empCount

    def displayEmployee(self):
        '打印员工信息'
        print "Name:", self.name, ", Salary:", self.salary

# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)

emp = Employee("yesco", "100")
emp.displayCount()
emp.displayEmployee()
# 增加一个属性
emp.age = 8
print "Age:", emp.age
print "Age:", getattr(emp, 'age')    # 返回 'age' 属性的值
# 删除一个属性
del emp.age
# 判断age属性是否存在
print "has age :", hasattr(emp, "age")
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
