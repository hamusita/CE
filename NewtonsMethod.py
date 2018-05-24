import sys


def func1(x):
    return (x**3 - 3 * x**2 + 9 * x - 8)


def func2(x):
    return (3 * x**2 - 6 * x + 9)


def input_num():
    s = "初期近似値を入力してください : "
    k = 1
    while 1:
        n = input(s)
        if len(n) == 1:
            ls = list(map((lambda x: x.isdigit() or (
                x[0] == "-" and x[1::].isdigit())), n))
            if False in ls:
                print("数値以外が入力されています")
                continue
            else:
                return int(n)
        else:
            print("不正な入力です")
            continue
        if k > 10:
            print("入力を一定数失敗したためプログラムを終了します")
            sys.exit()


def cal():
    pass


def main():
    n = input_num()


if __name__ == '__main__':
    main()
