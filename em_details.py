class COMPANY:
    em_id=[]
    em_name=[]
    em_salary=[]
    em_dis=[]


    def em_details(self,salary):
        self.em_salary.append(salary)


class SALARIES(COMPANY):
    def manager(self,id,name,dis):
        self.em_id.append(id)
        self.em_name.append(name)
        self.em_dis.append(dis)
        for y in range (len(self.em_id)):
            pass
        print(f" id of employee : {self.em_id[y]}")
        print(f" name of employee : {self.em_name[y]}")
        print(f" designation of employee : {self.em_dis[y]}")
        for x in self.em_salary:
            pay_scale=x+(x*18/100)
        print(f"pay scale of manager : {pay_scale}")
        self.status="clear"
    

    def tester(self,id,name,dis):
        self.em_id.append(id)
        self.em_name.append(name)
        self.em_dis.append(dis)
        for z in range (len(self.em_id)):
            pass   
        print(f" id of employee : {self.em_id[z]}")
        print(f" name of employee : {self.em_name[z]}")
        print(f" designation of employee : {self.em_dis[z]}")
        for x in self.em_salary:
            pay_scale=x+(x*16/100)
        print(f"pay scale of tester : {pay_scale}")
        self.status="clear"


    def developer(self,id,name,dis):
        self.em_id.append(id)
        self.em_name.append(name)
        self.em_dis.append(dis)
        for i in range (len(self.em_id)):
            pass
        print(f" id of employee : {self.em_id[i]}")
        print(f" name of employee : {self.em_name[i]}")
        print(f" designation of employee : {self.em_dis[i]}")
        for x in self.em_salary:
            pay_scale=x+(x*14/100)
        print(f"pay scale of developer : {pay_scale}")
        self.status="clear"


company=COMPANY()
company.em_details(12000)

pay=SALARIES()
pay.manager("02454432","afroz","manager")
pay.tester("2424343","subhani","tester")
pay.developer("534234","sayyad","developer")