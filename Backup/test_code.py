from datetime import datetime
import os


current_time = datetime.now()
print(current_time.month)


os.makedirs('./{0}' .format(current_time.month))
