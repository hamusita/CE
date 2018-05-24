import sys


def func(x):
    return (x**3 - 3 * x**2 + 9 * x - 8)


def input_num():
    s = "f(a)*f(b) < 0 となる[a,b]をスペース区切りで入力してください : "
    k = 1
    while 1:
        n = list(input(s).split())
        if len(n) == 2:
            ls = list(map((lambda x: x.isdigit() or (
                x[0] == "-" and x[1::].isdigit())), n))
            if False in ls:
                print("数値以外が入力されています")
                continue
            else:
                a, b = map(int, n)
                if func(a) * func(b) < 0:
                    return max(a, b), min(a, b)
                else:
                    print("f(a)*f(b) < 0 を満たしていません")
                    continue
        else:
            print("不正な入力です")
            continue
        if k > 10:
            print("入力を一定数失敗したためプログラムを終了します")
            sys.exit()


def cal(a, b):
    k = 0
    while(a - b >= 0.00001):
        c = (a + b) / 2
        if func(a) * func(c) > 0:
            a = c
        else:
            b = c
        if k > 100:
            return "解は100回以内には収束しませんでした"
    return (a + b) / 2


def out(x):
    if isinstance(x, float):
        print("有効桁数５桁で収束しました")
        print(" x = %f," % x)
    else:
        print(x)


def main():
    a, b = input_num()
    c = cal(a, b)
    out(c)


if __name__ == '__main__':
    main()
