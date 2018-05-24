#%%
import numpy as np
from matplotlib import pyplot


def input_num():
    n = int(input("補間点の個数を入力:n = "))
    print("続いて補間点の座標を入力してください")
    li = []
    for i in range(n):
        x = float(input("x%d = " % (i + 1)))
        y = float(input("y%d = " % (i + 1)))
        li.append((x, y))
    x = float(input("指定する点は？ : x = "))
    print(li, x)
    print("Ok. 入力を受け付けました")
    return li, x
    

def cal(li, x):
    s = 0.0
    for i in range(len(li)):
        seki = 1.0
        for j in range(len(li)):
            if j != i:
                seki *= (x - li[j][0]) / (li[i][0] - li[j][0])
        s += seki * li[i][1]
    return (x, s)


def val(li, x):
    y = []
    for i in x:
        y = np.append(y, cal(li, i)[1])
    return y


def main():
    li, x = input_num()
    x, y = cal(li, x)
    print("x = %f にて y = %f" % (x, y))
    x = np.linspace(-5, 5, 1000)
    y = val(li, x)

    pyplot.plot(x, y)
    pyplot.show()


if __name__ == '__main__':
    main()


