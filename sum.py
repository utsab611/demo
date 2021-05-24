
def sum(i):
    if i==1:
        return i
    else:
        return sum(i-1)+i

print(sum(10))        