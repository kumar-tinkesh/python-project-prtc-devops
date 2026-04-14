class Employee:
    company = 'ABC'
    bonus_amount  = 5000
    pay_rise_percent = .025

    def __init__(self, name, pay, role):
        self.name = name 
        self.pay = pay 
        self.role = role 

    def show_pay_with_bonus(self):
        total_pay = self.pay + Employee.bonus_amount
        return total_pay
    
    def increased_pay(self):
        self.pay += self.pay * Employee.pay_rise_percent
        return self.pay
    
    @classmethod
    def new_total_pay(cls, new_bonus_amount):
        cls.bonus_amount = new_bonus_amount

    @classmethod
    def new_incresed_pay(cls, new_pay_rise_percent):
        cls.pay_rise_percent = new_pay_rise_percent


rav = Employee('Rav', 50000,'Developer')
# print(vars(rav))
# print(rav.company)
# print(rav.bonus_amount)
Employee.new_total_pay(12000)
print(rav.show_pay_with_bonus())
Employee.new_incresed_pay(.5)
print(rav.increased_pay())