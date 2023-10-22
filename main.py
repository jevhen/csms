import item
import time
import data

# TODO: write some adequate tests.
# Sample item production time
#production_time: int = 1697975760
# Sample item expire time
#expire_time: int = 1698926160

# Current time
current_time: int = int(time.time())
week_in_seconds: int = 604800
# Modeling the situation where product ~66.6% expired
#production_time: int = current_time - week_in_seconds
#expire_time: int = current_time + (week_in_seconds / 2)
# Modeling the situation where we at 50% of 100 day expiring time
production_time: int = current_time - 4320000
expire_time: int = current_time + 4320000


bottle_milk: item.store_item = item.store_item(production_time, expire_time, data.dairy)
print(bottle_milk.exp_percentage_step)
print(bottle_milk.get_current_depr_percentage(bottle_milk.exp_date))
print(bottle_milk.threshold_reminder_time)