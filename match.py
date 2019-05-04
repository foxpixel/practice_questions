
runs = 0
score = []
for i in range(6):
    x = input("Enter decision %d : " % (i+1))
    if x.isdigit():
        x = int(x)
        score.append(x)
    while x == "Wd" or x == "Nb":
        score.append(x)
        x = input("Enter decision %d : " % (i+1))
        if x.isdigit():
            x = int(x)
            score.append(x)
            break
        elif x == "Wi":
            score.append(x)
            break
        else:
            pass
    if x == "Wi":
        score.append(x)

print(score)
for i in score:
    if i == "Wd" or i == "Nb":
        runs += 1
    elif x == "Wi":
        pass
    else:
        runs += i
print(runs)
