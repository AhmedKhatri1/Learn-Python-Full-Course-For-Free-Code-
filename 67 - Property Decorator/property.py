class Employee:
    salary = 25000
    salary_bonus = 20000
    company = "Ak"

    @property
    def total_salary(self):
        return self.salary + self.salary_bonus
    @total_salary.setter
    def total_salary(self,a):
        self.salary_bonus= a - self.salary

e = Employee()
print("The total salary with bonuns is :",e.total_salary)
e.total_salary = 60000
print(e.salary)
print(e.salary_bonus)