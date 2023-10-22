import time
import data

class store_item():
    def __init__(self, prod_date: int, exp_date: int, category: data.item_category):
        self.prod_date = prod_date
        self.exp_date = exp_date
        self.exp_percentage_step: float = (exp_date - prod_date) / 100 # Step in seconds for 1% item deprecation
        self.threshold_reminder_time: int = prod_date + (self.exp_percentage_step * category.depr_threshold)

    def get_current_depr_percentage(self, exp_date):
        return int( 100 - (exp_date - int(time.time())) / self.exp_percentage_step)
    
