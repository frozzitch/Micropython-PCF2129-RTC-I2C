
def timenow(i2c):

    secs = i2c.readfrom_mem(0x51, 0x02, 1)
    mins = i2c.readfrom_mem(0x51, 0x03, 1)
    hours = i2c.readfrom_mem(0x51, 0x04, 1)

    return(
        (str((hours[0] & 0x30)>>4) + (str((hours[0] & 0x0F)) + ":" + str(((mins[0] & 0x70)>>4)) + str((mins[0]  & 0x0F)) + ":" + str(((secs[0] & 0x70)>>4)) + str((secs[0] & 0x0F))))
           )

def datenow(i2c):

    day = i2c.readfrom_mem(0x51, 0x05, 1)
    month = i2c.readfrom_mem(0x51, 0x07, 1)
    year = i2c.readfrom_mem(0x51, 0x08, 1)

    return(
        (str((day[0] & 0x30)>>4) + str(day[0] & 0x0F) + "." + (str((month[0] & 0x10)>>4)) + (str(month[0] & 0x0F)) + ".20" + str((year[0] & 0xF0)>>4) + str(year[0] & 0x0F))
           )

def day(i2c):

    weekday = i2c.readfrom_mem(0x51, 0x06, 1)
        
    if weekday[0] == 0:
        dayname = "SUN"
    elif weekday[0] == 1:
        dayname = "MON"
    elif weekday[0] == 2:
        dayname = "TUE"          
    elif weekday[0] == 3:
        dayname = "WED"
    elif weekday[0] == 4:
        dayname = "THU"
    elif weekday[0] == 5:
        dayname = "FRI"
    elif weekday[0] == 6:
        dayname = "SAT"
    else:
        dayname = "Invalid value (0-6)"
    

    return(
        dayname
           )
 
def daynum(i2c):
    return i2c.readfrom_mem(0x51, 0x06, 1)

def rtcset(HH,MM,SS,dd,mm,yy,d,i2c):
    buf = bytearray(7)
    buf[0] = int("0x" + str(SS))
    buf[1] = int("0x" + str(MM)) 
    buf[2] = int("0x" + str(HH)) 
    buf[3] = int("0x" + str(dd)) 
    buf[4] = int("0x" + str(d))
    buf[5] = int("0x" + str(mm)) 
    buf[6] = int("0x" + str(yy)) 
    
    i2c.writeto_mem(0x51, 0x03, buf) 
    

