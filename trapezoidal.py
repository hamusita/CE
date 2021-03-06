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
    ans = f.sym.subs([(x, a)]) * h / 2 + f.sym.subs([(x, b)]) * h / 2 
    for i in drange(a + h, b + h, h): 
        ans += f.sym.subs([(x, i)]) * h
    print("ans = %f" % ans)

def drange(begin, end, step):
    n = begin
    while n + step < end:
        yield n
        n += step

if __name__ == '__main__':
    main()