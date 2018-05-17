import time

'''
https://github.com/AllenDowney/ThinkPython2/issues/18
'''

hora_greenwich = time.time()

seconds_in_one_day = 24 * 60 * 60
seconds_in_one_hours = 60 * 60 
seconds_in_one_minute = 60

days = hora_greenwich // seconds_in_one_day
years = days // 365
hours = (hora_greenwich % seconds_in_one_day)


print(days, years)