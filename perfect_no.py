s = 0
p = []
n = int(input("enter a no"))
for i in range(1, n):
    if n % i == 0:
        p.append(i)
    else:
        pass
print(p)
for i in p:
    s += i
print(s)
if s == n:
    print("PERFECT_NO")
else:
    print("NOT A PERFECT NO")
