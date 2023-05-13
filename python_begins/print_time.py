import time
timestamp = int(time.strftime('%H:%M:%S'))
print("The time is:", timestamp)
hours = int(time.strftime('%H'))
print("The hours is :", hours)
minuts = time.strftime('%M')
print("The minutes is :", minuts)
Second = time.strftime('%S')
print("the second is: ", Second)
# if(timestamp > 0 && timestamp < 12):
#     print("good morning")
# else if(houtimestamprs>12&&timestamp<15):
if(timestamp > 0 and timestamp < 12):
