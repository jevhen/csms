import time

class store_item():
    def __init__(self, prod_date, exp_date):
        self.prod_date = prod_date
        self.exp_date = exp_date
        self.exp_percentage = time.time()
    
    # TODO: define method to calculate current percentage of expiring
    # TODO: define method to get corellation "UTC seconds - 1% of exp"
    #def append_expitation_percentage(self, ):
