# http://59.23.150.58/30stair/change/change.php?pname=change
money = int(input())
charge = 1000 - money

print(int(charge / 100), int(charge % 100 / 50), int(charge % 100 % 50 / 10))
