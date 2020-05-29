"""
	Buil in module
	--- contoh waktu
	documentasinya bisa dilihat di websitenya python
"""

import datetime

# print(datetime.datetime.now())

# #atau membuat tangal kita sendiri
# date = datetime.datetime(1999,8,10)
# print(date)

#atau membuat tangal degan format
date = datetime.datetime.now()
print(date.strftime("%Y %B %d"))