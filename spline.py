
def input_num():
    n = int(input("補間点の個数を入力:n = "))
    print("続いて補間点の座標を入力してください")
    li = [[],[]]
    for i in range(n):
        li[0].append(float(input("x%d = " % (i + 1))))
        li[1].append(float(input("y%d = " % (i + 1))))
    c = []
    c.append(float(input("全区間の左端点における１次微分係数は？ : a = ")))
    c.append(float(input("全区間の右端点における１次微分係数は？ : b = ")))
    print(li, c)
    print("Ok. 入力を受け付けました")
    return li, c


def main():
    li, c = input_num()

if __name__ == '__main__':
    main()