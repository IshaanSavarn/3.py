# parent class
class Person( object ):

    # _init__ is known as the constructor 
    def __init__(self,name,idnumber):
        self.name = name 
        self.idnumber = idnumber
        def display(self):
            print(self.name)
            print(self.idnumber)

    # child class
    class Employee( Person ):
        def __init__(self,name,
            idnumber, salary, post):
            self.salary = salary
            self.post = post

            # invoking the __init__ of the parent class
            Person,__init__(self, name,idnumber)

            # creation of an object variable or an instance
            a = Employee('Shivangi',20210403,1500, intern)

            b= Employee('Rahul', 20210403 2500 'Manager')
            c= Employee('Ravi', 20210403,3500 "Ceo")

            # calling a function of the class Person using its instance
            a.display( )
            b.display( )
            c.display( )
            
