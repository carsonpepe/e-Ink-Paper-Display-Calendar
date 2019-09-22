def monthName(arg):
    month = {
        1: ("January", 98),
        2: ("Februray", 98),
        3: ("March", 110),
        4: ("April", 110),
        5: ("May", 125),
        6: ("June", 120),
        7: ("July", 120),
        8: ("August", 108),
        9: ("September", 95),
        10: ("October", 100),
        11: ("November", 98),
        12: ("December", 98)
        }
    return month.get(arg, "Invalid Month")

def time_y_coord(hour, minute): #pass both paramteres as ints
    y_min = {
        9: 64,
        10: 128,
        11: 192,
        12: 256,
        1: 319,
        2: 383,
        3: 447,
        4: 511,
        5: 575
        }
    num = y_min.get(hour, None)
    if num is None:
        return None
    if num != 256:
        if minute < 20:
            return num + minute
        elif minute >= 20 and minute < 30:
            return num + minute + 1
        elif minute >= 30 and minute < 40:
            return num + minute + 2
        elif minute >= 40 and minute < 50:
            return num + minute + 3
        elif minute >= 50:
            return num + minute + 4
        else:
            raise ValueError('Minute value must be between 0 and 60 inclusive')
    else:
        if minute < 30:
            return num + minute
        elif minute >= 30 and minute < 40:
            return num + minute + 1
        elif minute >= 40 and minute < 50:
            return num + minute + 2
        elif minute >= 50:
            return num + minute + 3
        else:
            raise ValueError('Minute value must be between 0 and 60 inclusive')

def am_or_pm(arg):
    try:
        arg1 = int(arg) - 5
        if (arg1 < 12):
            t = 'am'
        elif (arg1 >= 12):
            t = 'pm'
        return t
    except:
        raise ValueError('Invalid input')

def dayFix(day, hour):
    if (int(hour) <= 4):
        return str(int(day) - 1)
    return str(int(day))
    
def hourFix(arg):
    hour = int(arg) - 5  #imported clock is 5 hours ahead Chicago time
    if hour - 12 > 0:
        return str(hour - 12)
    return str(hour)

#def minuteFix(arg):
#    min = int(arg) + 1  #accounts for approximate time it takes to buffer screen
#    if min < 10:
#        return '0' + str(min)
#    else:
#        return str(min)