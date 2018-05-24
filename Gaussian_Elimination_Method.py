import sys
import numpy as np


# 入力受付
def input_num(s, i):
    while 1:
        n = list(input(s).split())
        if len(n) == i:
            ls = list(map((lambda x: x.isdigit() or (
                x[0] == "-" and x[1::].isdigit())), n))
            print(ls)
            if False in ls:
                print("数値以外が入力されています")
                continue
            else:
                return list(map(float, n))
        else:
            print("不正な入力です")
            continue


# 行の入れ替え
def transport(matrix, k, lg):
    m = k
    # 係数がゼロじゃない要素を選択
    axes = [x for x in range(lg)]
    print(axes, lg)
    for i in range(k, lg):
        if abs(matrix[m][k]) < abs(matrix[i][k]):
            m = i
    print("Exchange %d and %d columns" % (k, m))
    axes[k], axes[m] = axes[m], axes[k]
    print(axes)
    # 行の交換
    print(matrix, "\ntransport")
    print(matrix.transpose(axes))
    print(matrix, "\ntransport fin \n")

    return matrix


def cal(matrix):
    x = []  # ans
    cal = np.array(matrix)
    lg = len(matrix)
    cal = cal[cal[:, 0].argsort()][::-1]
    print(cal)

    # 上三角型連立1次方程式の対角化
    for i in range(lg):
        p = cal[i][i]
        if abs(p) < 1.0e-6:
            print("一意解を持ちません")
            sys.exit()
        print(cal[i] / p, " = cal[%d]\n" % i)
        cal[i] = cal[i] / p
        print(cal, "\n")
        for j in range(i, lg):
            if i != j:
                cal[j] = cal[j] - cal[i] * cal[j][i]
        print(cal, "\n")

    # 逆進代入
    for i in range(lg - 1, -1, -1):
        s = 0.0
        m = cal[i][::-1]
        print(m, "= m")
        for j in range(1, len(m) - 1):
            if m[j] == 1:
                break
            else:
                s += m[j] * x[::-1][j - 2]
                print("     s += m[%d] * x[%d - 2]" % (j, j))
        print("     x[%d] = %f - %f \n" % (i, m[0], s))
        x.append(m[0] - s)
        print(x, "= x\n")

    return x[::-1]


def out(n, x):
    print("")
    for i in range(0, n):
        print("x(%d) = %5.6f" % (i + 1, x[i]))
    print("")


def main():
    print("ガウスの消去法による連立方程式の解法")
    while 1:
        a = input("連立方程式の次元数 : ")
        if a.isdigit():
            n = int(a)
        else:
            continue

        matrix = []
        print("係数をスペース区切りで入力してください")
        for i in range(n):
            ls = input_num("%d行目 : " % (i + 1), n + 1)
            matrix.append(ls)

        if input("\n正しく入力できましたか？ y or n : ") == "y":
            break

    x = cal(matrix)
    out(n, x)
    print("fin.\n")
    return 0


if __name__ == "__main__":
    main()
