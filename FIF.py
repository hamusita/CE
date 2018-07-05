import numpy as np
import pandas as pd

def input_num():
    n = int(input("補間点の個数を入力:n = "))
    print("続いて補間点の座標を入力してください")
    li = [[],[]]
    for i in range(n):
        li[0].append(float(input("x%d = " % (i + 1))))
        li[1].append(float(input("y%d = " % (i + 1))))
    x = float(input("指定する点は？ : x = "))
    print(li, x)
    print("Ok. 入力を受け付けました")
    return li, x
    

def diff(li):
    for i in range(1, len(li[0])):
        li.append([])
        for j in range(0, len(li[0]) - i):
            li[i + 1].append((li[i][j + 1] - li[i][j]))
    return li


def cal(li, x):
    k = (x - li[0][0]) / (li[0][1] - li[0][0])
    s, t = li[1][0], k
    for j in range(2,len(li)):
        s += li[j][0] * t
        t *= (k - j + 1) / j
    #print(t, s)
    return s


def main():
    li, x = input_num()
    li = diff(li)
    f = cal(li, x)
    print("\n f(%f) = %f \n" % (x, f))
    df = pd.DataFrame(li).T
    print(df)


if __name__ == '__main__':
    main()