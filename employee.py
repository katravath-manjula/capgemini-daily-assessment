class Employee:
    def __init__(self,name,id,dept):
        self.n=name
        self.id=id
        self.dep=dept
        print(f"employee name : {self.n}  \n Id: {self.id} \n Department:{self.dep}\n")

ob=Employee("annu",2564,"Cse")
ob2=Employee("Deepu",345,"aiml")
print(ob,ob2)   