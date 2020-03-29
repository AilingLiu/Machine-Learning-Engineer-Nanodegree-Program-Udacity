class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary, \
    pants_sold=[], total_sales=0):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = pants_sold
        self.total_sales = total_sales

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for pant in self.pants_sold:
            print(f'color: {pant.color}, waist_size: {pant.waist_size}, \
            length: {pant.length}, price: {pant.price}')

    def calculate_sales(self):
        for pant in self.pants_sold:
            self.total_sales+=pant.price
        return self.total_sales

    def calculate_commission(self,percentage):
        return self.total_sales*percentage
