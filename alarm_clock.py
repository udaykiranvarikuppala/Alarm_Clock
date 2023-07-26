import time
import winsound

t = time.localtime(time.time())
now_time = time.asctime(t)
print("Now it is", now_time)

print("Please enter the time  ")
entered_time = input("enter time ")

final_output = ""
for i in range(len(entered_time)):
    if ":" in entered_time[i] or "-" in entered_time[i] or "/" in entered_time[i]:
        final_output = final_output
    else:
        final_output = final_output + entered_time[i]

entered_second = int(final_output[-2:])
entered_minute = int(final_output[-4:-2])
entered_hour = int(final_output[:2])
#print(entered_second,entered_hour,entered_minute,final_output)

now_hour = time.strftime("%H")
now_minute = time.strftime("%M")
now_second = time.strftime("%S")

second = 0
if entered_second >= int(now_second):
    second = entered_second - int(now_second)
    if entered_minute >= int(now_minute):
        second = second + ((int(entered_minute)) - (int(now_minute)))*60
        if entered_hour >= int(now_hour):
            second = second + (((int(entered_hour)) - (int(now_hour)))*3600)
        else:
            second = str("Invalid")
    else:
        second = (((int(entered_minute)) + 60) - (int(now_minute)))*60
        entered_hour = (int(entered_hour)) - 1
        if entered_hour >= int(now_hour):
            second = second + (((int(entered_hour)) - (int(now_hour)))*3600)
        else:
            second = str("Invalid")

else:
    second = (60 + (int(entered_second))) - (int(now_second))
    entered_minute = (int(entered_minute)) - 1
    if entered_minute >= int(now_minute):
        second = second + ((int(entered_minute)) - (int(now_minute)))*60
        if entered_hour >= int(now_hour):
            second = second + (((int(entered_hour)) - (int(now_hour)))*3600)
        else:
            second = str("Invalid")
    else:
        second = (((int(entered_minute)) + 60) - (int(now_minute)))*60
        entered_hour = (int(entered_hour)) - 1
        if entered_hour >= int(now_hour):
            second = second + (((int(entered_hour)) - (int(now_hour)))*3600)
        else:
            second = str("Invalid")


print("Time", now_hour, now_minute, now_second)
print(second, "seconds")
time.sleep(second)
print("Alarm is ringing")
beet = [500, 600, 700, 550, 450, 500, 520, 570, 500, 500, 500, 500]
for sound in range(len(beet)):
    winsound.Beep(beet[sound], 100)
