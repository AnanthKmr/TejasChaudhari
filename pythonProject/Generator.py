def countdown(n):
    while n>0:
        yield n
        n-=1
for n in countdown(5):
    print(n)