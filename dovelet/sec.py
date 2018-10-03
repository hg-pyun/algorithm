# http://59.23.150.58/30stair/sec/sec.php?pname=sec
val = int(input())

second = 60
min = second * 60
day = min * 24

print(int(val / day), int(val % day / min), int(val % day % min / second), int(val % day % min % second))
