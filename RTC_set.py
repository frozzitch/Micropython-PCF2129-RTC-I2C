import machine
from PCF2129RTC import rtcset, timenow, datenow, day

sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=100000)



rtcset(11,22,33,4,3,25,2,i2c) #Hour, Min, Sec, Day, Month, Year, Day in week (0-6, SUN, MON, TUE...)

print("RTC SET: " + timenow(i2c) + "," + datenow(i2c) + "," + day(i2c))
