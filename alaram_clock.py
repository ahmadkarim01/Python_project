# I am creating an acronyms using python.
# user_input = str(input("Enter a phrase: "))
# text = user_input.split()
# a = " "
# for i in text:
#     a = a + str(i[0]).upper()
# print(a)

# user_input = str(input("Enter a phrase:"))
# text = user_input.split()
# health = " "
# for i in text:
#     health = health + str(i[1]).upper()
#     print(health)

# //////////////////////////////////////////////////////////
# alaraming clock by using 

from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break


# //////////////////////////////////////////////////////////
# Generate a password
import random
passlen = int(input("Enter the length of password: "))
s = "aahuiehjajlr2343#$%45^$56bj25k354242452234)(*&&^%^)"
p = "".join(random.sample(s,passlen))
print(p)