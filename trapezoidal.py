from sympy import *

def main():
    x = symbols('x')
    s = input("pythonの規則に準拠した数式を入れてください : ")
    f = x
    exec('f = ' + s )
    print("積分区間[a,b]を入力してください")
    a, b = map(int, input("a,b = ").split())
    d = int(input("分割数を入力 : v = "))
    h = (b - a) / d
    print(a, b, d, h)
    ans = f.subs([(x, a)]) * h / 2 + f.subs([(x, b)]) * h / 2 
    for i in drange(a + h, b, h): 
        ans += f.subs([(x, i)]) * h
        print()
    print("ans = %f" % ans)

def drange(begin, end, step):
    n = begin
    while n+step < end:
        yield n
        n += step

if __name__ == '__main__':
    main()