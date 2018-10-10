import sympy as sym

def main():
    x = sym.symbols('x')
    s = input("pythonの規則に準拠した数式を入れてください : ")
    f = x
    exec('f = ' + s)
    print(f)
    print("積分区間[a,b]を入力してください")
    a, b = map(float, input("a,b = ").split())
    n = int(input("分割数を入力 : v = "))
    h = (b - a) / n
    print(a, b, n, h)
    ans = (f.subs([(x, a)]) + f.subs([(x, b)])) * h / 3
    #print(f.subs([(x, a)]) + f.subs([(x, b)]))
    for i in drange(a + h, b + 2 * h, 2 * h):
        #print(i, f.subs([(x, i)]), i + h, f.subs([(x, i + h)]))
        ans += f.subs([(x, i)]) * 4 * h / 3
        ans += f.subs([(x, i + h)]) * 2 * h / 3
        last = i + h
    ans -= f.subs([(x, last)]) * 2 * h / 3
    print("ans = %f" % ans)

def drange(begin, end, step):
    n = begin
    while n + step < end:
        yield n
        n += step

if __name__ == '__main__':
    main()