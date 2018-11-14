"""Given seconds (int) calculate hours, minutes and seconds.
For example, given 80000 seconds that is 22 hours, 13 minutes and 20 seconds.
Hint 1: use integer division // and remainder %
Hint 2: we require that you create and output variables hours, minutes
and seconds but you will likely find an additional variable useful."""

sec = int(80000)     #"""input("Input seconds: ")"""
hour = int(sec)//3600
minute = int(sec)/60 - hour*60
minute = int(minute)
second = int(sec)-hour*3600-minute*60
second = int(second)

print(int(hour))
print(int(minute))
print(int(second))
