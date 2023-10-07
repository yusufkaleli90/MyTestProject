import time

remind = str(input("What should i remind you about? "))
minutes = float(input("In how many minutes? "))
time_sec = minutes * 60
time.sleep(time_sec)
print(remind)