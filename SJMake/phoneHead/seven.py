from phone import Phone
import random
p = Phone()

def getinputOperators(Operators):
    ydPhone = ['134','135','136','137','138','139','147','148','150','151','152','157','158','159','178','182','183','184','187','188','198']
    ltPhone = ['145', '131', '132', '130', '155', '156', '166', '171', '175', '176', '185', '186', '166','167']
    dxPhone = ['133','153','177','180','181','189','191','199']
    if Operators == '移动':
        return ydPhone
    elif Operators == '联通':
        return ltPhone
    elif Operators == '电信':
        return dxPhone
    else:
        print("运营商输入有误")
        exit()

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        # print(path+'创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+'目录已存在')
        return False

def randomSeven(province,inputOperators):
    print("正在生成.....")
    Operators = getinputOperators(inputOperators)
    bb = f"{province}{inputOperators}生成结果\{province}地级市"
    mkdir(bb)

    for x in Operators:
        num = 9999
        while num > 999:
            info = p.find(str(x) + str(num))
            if info == None:
                num -= 1
            else:
                if info["province"] == province:
                    city = info["city"]
                    phone = info["phone"]
                    path = bb+f"\{city}.txt"

                    #地级市
                    with open(path, "a")as f2:  # f2为文件描述符
                        suffix = ''
                        for q in range(4):
                            suffix = suffix + str(random.randint(0, 9))
                        phoneNum = str(phone) + str(suffix)
                        f2.write(phoneNum + "\n")

                        #总计
                    path = f"{province}{inputOperators}生成结果\{province}{inputOperators}手机号总合.txt"
                    with open(path, "a")as f2:  # f2为文件描述符
                        suffix = ''
                        for w in range(4):
                            suffix = suffix + str(random.randint(0, 9))
                        phoneNum = str(phone) + str(suffix)
                        f2.write(phoneNum + "\n")
            num -= 1



















