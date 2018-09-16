# http://59.23.150.58/30stair/swap/swap.php?pname=swap
a,b = map(int, input().split())
temp = a
a = b
b = temp
print(a, b)