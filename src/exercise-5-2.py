def check(a, b, c, n):
    if n > 2 and a^n + b^n == c^n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("No, that doesn't work.")

n = int(input("n: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

check(a,b,c,n)
