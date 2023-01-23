
class COMPANY:
    employee=[]
    no_employees=[]
    salary=[]

    def add_employee(self,disignation,quantity,salary):
        self.employee.append(disignation)
        self.no_employees.append(quantity)
        self.salary.append(salary)

    def payment(self):
        total=0
        for i in range (len(self.salary)):
            total+=self.no_employees[i]*self.salary[i]
        return total

class SALARIES(COMPANY):
    def manager(self):
        print("salaries of manager level employees :")
        id=[i for i in range(12332,12433)]
        for y in id:
            print(f"id of the manager : {y}")
            for x in self.salary:
                pay_scale=x+(x*18/100)
            print(f"pay scale of manager with id {y} : {pay_scale}")
        self.status="clear"

    def tester(self):
        print("salaries of tester level employees :")
        id=[i for i in range(10045,10146)]
        for y in id:
            print(f"id of the tester : {y}")
            for x in self.salary:
                pay_scale=x+(x*16/100)
            print(f"pay scale of tester with id {y} : {pay_scale}")
        self.status="clear"

    def developer(self):
        print("salaries of developer level employees :")
        id=[i for i in range(13241,13342)]
        for y in id:
            print(f"id of the developer : {y}")
            for x in self.salary:
                pay_scale=x+(x*14/100)
            print(f"pay scale of developer with id {y} : {pay_scale}")
        self.status="clear"





company=COMPANY()
company.add_employee("manager",100,1200000)
company.add_employee("tester",100,1200000)
company.add_employee("developer",100,1200000)
print(company.payment())

pay=SALARIES()
pay.manager()
pay.tester()
pay.developer()