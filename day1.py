# 用户身份验证
if __name__ == '__main__':
    num = 0
    while True:
        num += 1
        username = str(input("请输入你的用户名：\n"))
        password = int(input("请输入你的密码：\n"))
        if username != 'admin' and password != "123456":
            print('用户名或密码错误！')
            if num >= 3:
                print("连续登录%s次账户锁定" % num)
                break
        else:
            print("登录成功")
            break

# 输出乘法口诀表(九九表)
if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %d" % (j, i, i * j), end='\t')
        print()

if __name__ == '__main__':
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()
