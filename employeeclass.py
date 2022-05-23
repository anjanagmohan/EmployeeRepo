class Employee:
    def __init__(self,idno,name,loc,sal):
        self.idno=idno
        self.name= name
        self.loc=loc
        self.sal=sal
    def GetEmployee(self):
        print("Name:" + self.name + "ID No:" + str(self.idno) + "Branch:" + self.loc + "Salary:" + str(self.sal))
