# http://59.23.150.58/30stair/koi_watch/koi_watch.php?pname=koi_watch

h, m, s = map(int, input().split())
time = int(input())

cook_h = int(time / 3600)
cook_m = int(time % 3600 / 60)
cook_s = int(time % 3600 % 60)

result_s = int((s + cook_s) % 60)
result_m = int((m + cook_m + int((s + cook_s) / 60)) % 60)
result_h = int((h + cook_h + int((m + cook_m + int((s + cook_s) / 60)) / 60)) % 24)

print(result_h, result_m, result_s)