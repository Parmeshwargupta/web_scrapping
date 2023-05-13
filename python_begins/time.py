import time
today = int(time.strftime('%H,%M,%S').replace(',', ''))
print(today)
hour = int(time.strftime('%H'))
hour = int(input("Enter the hour:"))

if(hour > 0 and hour < 12):
    print("good morning")
elif(hour >= 12 and hour < 17):
    print("Good Afternoon")
if(hour >= 17 and hour < 0):
    print("Good night")
