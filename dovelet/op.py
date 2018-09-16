# http://59.23.150.58/30stair/op/op.php?pname=op
a, b = map(int, input().split())
print(str(a) + '+' + str(b) + '=' + str(a+b))
print(str(a) + '-' + str(b) + '=' + str(a-b))
print(str(a) + '*' + str(b) + '=' + str(a*b))
print(str(a) + '/' + str(b) + '=' + str(int(a/b)))
print(str(a) + '%' + str(b) + '=' + str(a%b))