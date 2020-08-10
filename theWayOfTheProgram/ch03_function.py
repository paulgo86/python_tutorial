import math
# print(math.pi)




# get time format
def get_time(totalSec):
    h = int(totalSec // (60 ** 2))
    m = s = 0
    leftSec = totalSec - (h * (60 ** 2))
    print('totalSec = ' + str(totalSec))
    print('h = ' + str(h))
    if leftSec > 0:
        m = int(leftSec // 60)
        s = int(leftSec % 60)
    result = str(h) + ':' + str(m) + ':' + str(s)
    return result

# speed standard ( kilometers / hour )
def get_time_by_distance(dist,speed):
    ratio = dist / speed
    sec = ratio * (60 ** 2)
    print(sec)
    result = get_time(sec)
    print(result)

# get_time_by_distance(1,20) # get time who run 1km with 20km/h speed.  0:3:0 - 3min


