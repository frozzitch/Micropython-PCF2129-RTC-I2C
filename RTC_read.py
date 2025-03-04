from PCF2129RTC import timenow, datenow, day, rtcset
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)

print (timenow(i2c))
print (datenow(i2c))
print (day(i2c))