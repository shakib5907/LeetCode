n = int(input())
count = 0

if n != 0:
    while n > 0:
        n = int(n / 10)
        count = count + 1
else:
    count = count + 1

print(count)