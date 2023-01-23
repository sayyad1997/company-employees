class COMPANY:
    employee=[]
    no_employees=[]
    salary=[]
    status="open"

    def add_employee(self,disignation,quantity,salary):
        self.employee.append(disignation)
        self.no_employees.append(quantity)
        self.salary.append(salary)

    def payment(self):
        total=0
        for i in range(len(self.salary)):
            total+=self.no_employees[i]*self.salary[i]
        return total

class SALARIES(COMPANY):
    def manager(self):
        print("salaries of manager level employees :")
        for x in self.salary:
            pay_scale=x+(x*18/100)
        print(f"pay scale of each manager : {pay_scale}")
        self.status="clear"

    def tester(self):
        print("salaries of tester level employees :")
        for x in self.salary:
            pay_scale=x+(x*16/100)
        print(f"pay scale of each tester : {pay_scale}")
        self.status="clear"

    def developer(self):
        print("salaries of developer level employees :")
        for x in self.salary:
            pay_scale=x+(x*14/100)
        print(f"pay scale of each developer : {pay_scale}")
        self.status="clear"

company=COMPANY()
company.add_employee("manager",5,1200000)
company.add_employee("tester",123,1200000)
company.add_employee("developer",103,1200000)
print(company.payment())

pay=SALARIES()
pay.manager()
pay.tester()
pay.developer()

        

