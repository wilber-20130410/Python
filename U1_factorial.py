#求数的乘阶

def factorial(x):
    m = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        m*=i
    return m

x = 10
v = factorial(x)
print("%d 的乘阶是%d" % (x, v))