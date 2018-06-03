
import numpy as np
from matplotlib import pyplot

def input_num():
    n = int(input("補間点の個数を入力:n = "))
    print("続いて補間点の座標を入力してください")
    li = [[],[]]
    for i in range(n):
        li[0].append(float(input("x%d = " % (i + 1))))
        li[1].append(float(input("y%d = " % (i + 1))))
    c = []
    c.append(float(input("全区間の左端点における１次微分係数は？ : C1 = ")))
    c.append(float(input("全区間の右端点における１次微分係数は？ : Cn = ")))
    print(li, c)
    print("Ok. 入力を受け付けました")
    return li, c

def cal(li, c):
    l = len(li[0])
    D = li[1][:]
    h = [(li[0][i + 1] - li[0][i]) for i in range(l - 1)]
    u = [((li[1][i + 1] - li[1][i]) / h[i]) for i in range(l - 1)]
    
    p = [[0] * (l + 1) for i in range(l)]

    p[0][0]         = 1
    p[l - 1][l - 1] = 1
    p[0][l]         = c[0]
    p[l - 1][l]     = c[1]

    for j in range(1, l - 1):
        p[j][j - 1] = h[j]
        p[j][j]     = 2 * (h[j - 1] + h[j])
        p[j][j + 1] = h[j - 1]
        p[j][l]     = 3 * (h[j] * u[j - 1] + h[j - 1] * u[j])

    p = Gauss_Jordan(p, l)

    #解をCにぶっ込む
    c = [p[i][l] for i in range(l)]
    b = [(3 * u[j] - 2 * c[j] - c[j + 1]) / h[j] for j in range(l - 1)]
    #b.append(-(3 * u[l - 2] - 2 * c[l - 2] - c[l - 1]) / h[l - 2])
    a = [(b[k + 1] - b[k]) / (3 * h[k]) for k in range(l - 2)]
    a.append((u[l - 2] - h[l - 2] * b[l - 2] - c[l - 2]) / (h[l - 2] ** 2))
    print(a, b)

    #結果出力
    for i in range(l - 1):
        print("S%d(x) = " % i)
        print("(%f)(x - %f) ** 3 + " % (a[i], li[0][i]))
        print("(%f)(x - %f) ** 2 + " % (b[i], li[0][i]))
        print("(%f)(x - %f)      + " % (c[i], li[0][i]))
        print("(%f)\n" % D[i])
    
    return a, b, c, D, l



def Gauss_Jordan(p, l):
    for i in range(l):
        q = p[i][i]
        for j in range(l + 1):
            p[i][j] = p[i][j] / q
        for k in range(l):
            g = p[k][i]
            if k != i:
                for j in range(l + 1):
                    p[k][j] = p[k][j] - g * p[i][j]
    
    return p

def spline(a, b, c, d, li, x):
    h, val = li[0], 0
    y = []
    for i in x:
        if not(i <= h[val + 1]):
            val += 1
            print(h[val + 1], val)
        y = np.append(y, a[val] * (i - h[val]) ** 3 + b[val] * (i - h[val]) ** 2 + c[val] * (i - h[val]) + d[val])
    return y

def main():
    li, c = input_num()
    a, b, c, d, l = cal(li, c)

    f = int(input("何分割する？ n = "))
    x = np.linspace(li[0][0], li[0][l - 1], f)
    y = spline(a, b, c, d, li, x)

    pyplot.plot(x, y)
    pyplot.show()

if __name__ == '__main__':
    main()
